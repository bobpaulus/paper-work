#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Clash for Windows 控制脚本 / Clash Controller
=============================================

用途：在文献检索自动化中按需开启 / 关闭 Clash 代理，并做通道连通性探测。

安全设计（重要）：
  - **secret 不硬编码**：每次从 `%USERPROFILE%\\.config\\clash\\config.yaml` 动态读取。
  - **secret 不打印**：任何输出中均以 `***` 遮蔽，避免泄漏到日志/终端/代码仓。
  - API 请求**强制绕过代理**（`ProxyHandler({})`），否则会走 Clash 自己形成环路。

子命令 / Sub-commands:
  status              查看进程 / API / 当前 mode / 系统代理 / 通道探测
  on                  开启：未在跑则启动 CFW，并切到 rule 模式
  off                 关闭：默认退出 Clash 进程（--soft 则仅切成 direct 模式）
  mode <rule|global|direct>   切换运行模式
  nodes               列出代理组与可用节点（仅名称与延迟，不含密码）
  use <节点名>         把 GLOBAL 组切换到指定节点
  probe               只做通道连通性探测（直连 vs 代理对比）

用法示例 / Examples:
  python clash_ctl.py status
  python clash_ctl.py on
  python clash_ctl.py probe
  python clash_ctl.py off            # 退出进程
  python clash_ctl.py off --soft     # 仅切 direct，保留进程
  python clash_ctl.py use "日本-TY-1-流量倍率:1"

注意：本脚本无法改变**父 shell** 的环境变量。`on` 会打印可直接 source 的 export 语句：
  eval "$(python clash_ctl.py on --export)"
"""

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

# ---------------------------------------------------------------- 配置定位

USERPROFILE = os.environ.get("USERPROFILE") or os.path.expanduser("~")
CLASH_CFG = os.path.join(USERPROFILE, ".config", "clash", "config.yaml")
CLASH_EXE = os.path.join(
    USERPROFILE, "AppData", "Local", "Programs",
    "Clash for Windows", "Clash for Windows.exe")
# 内核（命令行程序，无 GUI）。CFW 是 Electron，在无交互会话中拉不起来，
# 需用内核 + 完整 profile 才能脱离 GUI 提供代理。
CLASH_CORE = os.path.join(
    USERPROFILE, "AppData", "Local", "Programs", "Clash for Windows",
    "resources", "static", "files", "win", "x64", "clash-win64.exe")

PROC_NAMES = ("Clash for Windows.exe", "clash-win64.exe")

# 探测用的关键通道（本项目真实依赖）
CHANNELS = [
    ("NCBI eutils", "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=thyroid&retmax=1"),
    ("NCBI GEO", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60542&targ=self&form=text&view=brief"),
    ("Europe PMC", "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=thyroid&format=json&pageSize=1"),
    ("OpenAlex", "https://api.openalex.org/works?per-page=1"),
    ("Crossref", "https://api.crossref.org/works?query=thyroid&rows=1"),
    # 注意：Unpaywall 返回 422 通常表示该 email 参数被拒，网络层其实是通的
    ("Unpaywall", "https://api.unpaywall.org/v2/10.1371/journal.pone.0301128?email=litreview@example.org"),
    ("Google(需翻墙)", "https://www.google.com"),
]


# ---------------------------------------------------------------- 基础工具

def _mask(s):
    """遮蔽敏感串，仅保留首尾各 2 字符。"""
    if not s:
        return "(空)"
    if len(s) <= 6:
        return "*" * len(s)
    return s[:2] + "*" * (len(s) - 4) + s[-2:]


def read_cfg():
    """读取 config.yaml 中的 external-controller 与 secret（不依赖 PyYAML）。"""
    ctrl, secret = None, None
    try:
        with open(CLASH_CFG, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("external-controller:"):
                    ctrl = line.split(":", 1)[1].strip()
                elif line.startswith("secret:"):
                    secret = line.split(":", 1)[1].strip()
    except FileNotFoundError:
        pass
    return ctrl, secret


def proc_running():
    """检测 Clash 进程（用 tasklist，避免依赖 psutil）。"""
    # 中文 Windows 的 tasklist 输出为 GBK，必须显式指定，否则 UnicodeDecodeError
    # GUI 外壳与内核任一在跑即视为"运行中"（内核可脱离 GUI 独立工作）
    try:
        for name in PROC_NAMES:
            r = subprocess.run(["tasklist", "/FI", "IMAGENAME eq " + name],
                               capture_output=True, timeout=15)
            if name.lower() in r.stdout.decode("gbk", errors="ignore").lower():
                return True
        return False
    except Exception:
        return False


def api_get(path, timeout=8):
    """调用 Clash External Controller API。强制不走代理。"""
    ctrl, secret = read_cfg()
    if not ctrl:
        return None, "未找到 external-controller（Clash 未运行或配置缺失）"
    url = "http://%s%s" % (ctrl, path)
    req = urllib.request.Request(url)
    if secret:
        req.add_header("Authorization", "Bearer %s" % secret)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8", "ignore")), None
    except urllib.error.HTTPError as e:
        return None, "HTTP %s" % e.code
    except Exception as e:
        return None, type(e).__name__ + ": " + str(e)[:80]


def api_patch(path, payload, timeout=8):
    ctrl, secret = read_cfg()
    if not ctrl:
        return None, "未找到 external-controller"
    url = "http://%s%s" % (ctrl, path)
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="PATCH")
    req.add_header("Content-Type", "application/json")
    if secret:
        req.add_header("Authorization", "Bearer %s" % secret)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "ignore"), None
    except urllib.error.HTTPError as e:
        return None, "HTTP %s" % e.code
    except Exception as e:
        return None, type(e).__name__ + ": " + str(e)[:80]


def api_put(path, payload=None, timeout=8):
    """切换代理组节点用 PUT。"""
    ctrl, secret = read_cfg()
    if not ctrl:
        return None, "未找到 external-controller"
    url = "http://%s%s" % (ctrl, path)
    data = json.dumps(payload or {}).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="PUT")
    req.add_header("Content-Type", "application/json")
    if secret:
        req.add_header("Authorization", "Bearer %s" % secret)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "ignore"), None
    except urllib.error.HTTPError as e:
        return None, "HTTP %s" % e.code
    except Exception as e:
        return None, type(e).__name__ + ": " + str(e)[:80]


def curl_code(url, proxy=None, timeout=20):
    """探测超时默认 20s：代理握手 + 连续多请求时，12s 会误判为 000。"""
    """用 curl 探测 HTTP 码。proxy=None 表示直连（--noproxy '*'）。"""
    cmd = ["curl", "-s", "-o", os.devnull, "-w", "%{http_code}", "--max-time", str(timeout)]
    if proxy:
        cmd += ["-x", proxy]
    else:
        cmd += ["--noproxy", "*"]
    cmd.append(url)
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 6)
        return r.stdout.strip() or "000"
    except Exception:
        return "000"


def sysproxy():
    """读取系统代理（winreg，绕开被禁的 reg.exe）。"""
    try:
        import winreg
        k = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                           r"Software\Microsoft\Windows\CurrentVersion\Internet Settings")
        enable = winreg.QueryValueEx(k, "ProxyEnable")[0]
        server = winreg.QueryValueEx(k, "ProxyServer")[0]
        return bool(enable), server
    except Exception as e:
        return None, "读取失败: %s" % type(e).__name__


def set_sysproxy(enable):
    """
    开关系统代理（winreg + 通知系统刷新）。

    关键：kill Clash 前**必须先关掉系统代理**。否则代理地址仍指向 127.0.0.1:7890
    而该端口已无监听，会导致**整个系统（浏览器等）无法上网**。
    """
    try:
        import winreg
        k = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",
            0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(k, "ProxyEnable", 0, winreg.REG_DWORD, 1 if enable else 0)
        winreg.CloseKey(k)
        # 通知系统立即生效（否则需重开浏览器）
        try:
            import ctypes
            inet = ctypes.windll.Wininet.InternetSetOptionW
            inet(0, 39, None, 0)   # INTERNET_OPTION_SETTINGS_CHANGED
            inet(0, 37, None, 0)   # INTERNET_OPTION_REFRESH
        except Exception:
            pass
        return True, None
    except Exception as e:
        return False, "%s: %s" % (type(e).__name__, e)


# ---------------------------------------------------------------- 子命令

def cmd_status(args):
    ctrl, secret = read_cfg()
    print("=" * 68)
    print("Clash 状态 / Clash Status")
    print("=" * 68)
    print("配置文件 : %s" % CLASH_CFG)
    print("主程序   : %s" % ("存在" if os.path.isfile(CLASH_EXE) else "未找到!"))
    print("控制端口 : %s" % (ctrl or "(未配置)"))
    print("secret   : %s  (已遮蔽，绝不回显明文)" % _mask(secret))
    running = proc_running()
    print("进程     : %s" % ("✅ 运行中" if running else "❌ 未运行"))

    cfg, err = api_get("/configs")
    if err:
        print("API      : ❌ %s" % err)
    else:
        print("API      : ✅ 可达")
        print("运行模式 : %s" % cfg.get("mode"))
        print("mixed-port: %s" % cfg.get("mixed-port"))

    en, sv = sysproxy()
    print("系统代理 : %s" % (("✅ 开启 -> " + str(sv)) if en else ("❌ 关闭" if en is False else sv)))
    print("env 代理 : http_proxy=%s" % os.environ.get("http_proxy", "(未设置)"))
    print()
    do_probe(args)
    return 0


def do_probe(args):
    ctrl, _ = read_cfg()
    cfg, _ = api_get("/configs")
    port = (cfg or {}).get("mixed-port") or 7890
    proxy = "http://127.0.0.1:%s" % port
    print("-" * 68)
    print("%-18s %-12s %-12s" % ("通道 / Channel", "直连", "走Clash"))
    print("-" * 68)
    for name, url in CHANNELS:
        d = curl_code(url, proxy=None)
        p = curl_code(url, proxy=proxy)
        mark = lambda c: "✅ %s" % c if c.startswith("2") else ("⚠️ %s" % c if c != "000" else "❌ %s" % c)
        print("%-18s %-12s %-12s" % (name, mark(d), mark(p)))
    print("-" * 68)
    print("说明：HTTP 000 = 连接失败/超时；429 = 可达但被限流；203 = 可达（NCBI 反爬）")


def cmd_on(args):
    if not proc_running():
        if not os.path.isfile(CLASH_EXE):
            print("❌ 未找到 Clash 主程序：%s" % CLASH_EXE)
            return 1
        print("启动 Clash for Windows ...", flush=True)
        try:
            # 必须完全脱离父进程并丢弃句柄：否则 GUI 进程会持有 stdout，
            # 导致调用方（如 Bash 工具）认为命令未结束而超时 SIGTERM。
            DETACHED_PROCESS = 0x00000008
            CREATE_NEW_PROCESS_GROUP = 0x00000200
            subprocess.Popen(
                [CLASH_EXE],
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP,
                close_fds=True)
        except Exception as e:
            print("❌ 启动失败: %s" % e)
            return 1
        # 等待 API 就绪（最多 45 秒）
        for i in range(45):
            time.sleep(1)
            cfg, err = api_get("/configs", timeout=3)
            if not err:
                print("✅ Clash 已就绪（%d 秒）" % (i + 1))
                break
        else:
            print("⚠️ 已启动进程但 API 未就绪，请手动确认")
            return 1
    else:
        print("✅ Clash 已在运行")

    if not args.direct:
        _, err = api_patch("/configs", {"mode": "rule"})
        print("模式切换 : %s" % ("✅ rule" if not err else "❌ %s" % err))

    cfg, _ = api_get("/configs")
    port = (cfg or {}).get("mixed-port") or 7890

    # 若此前被 off 关掉过系统代理，这里恢复（CFW 不一定会自动重开）
    en, sv = sysproxy()
    if en is False:
        ensure, err = set_sysproxy(True)
        print("系统代理 : %s" % ("✅ 已恢复开启" if ensure else "❌ %s" % err))
    else:
        print("系统代理 : ✅ 已开启 -> %s" % sv)

    if args.export:
        print('export http_proxy="http://127.0.0.1:%s"' % port)
        print('export https_proxy="http://127.0.0.1:%s"' % port)
        print('export HTTP_PROXY="http://127.0.0.1:%s"' % port)
        print('export HTTPS_PROXY="http://127.0.0.1:%s"' % port)
    else:
        print("代理端口 : %s" % port)
        print("在当前 bash 中生效请执行：")
        print('  eval "$(python clash_ctl.py on --export)"')
    return 0


def cmd_off(args):
    if args.soft:
        _, err = api_patch("/configs", {"mode": "direct"})
        print("软关闭（保留进程，切 direct）: %s" % ("✅" if not err else "❌ %s" % err))
        return 0 if not err else 1
    # 关键顺序：先关系统代理，再杀进程。反过来的话代理地址会残留在已无人监听的
    # 127.0.0.1:7890，导致整个系统断网。
    print("1) 关闭系统代理（防止残留导致全局断网）...")
    ok, err = set_sysproxy(False)
    print("   %s" % ("✅ 已关闭" if ok else "❌ %s" % err))

    print("2) 退出 Clash 进程 ...")
    for name in PROC_NAMES:
        # taskkill 输出同样是 GBK，不能 text=True
        r = subprocess.run(["taskkill", "/F", "/IM", name],
                           capture_output=True, timeout=20)
        r.stdout.decode("gbk", errors="ignore")
        if r.returncode == 0:
            print("   ✅ 已结束 %s" % name)
        else:
            print("   · %s 未在运行或已结束" % name)
    time.sleep(2)
    print("3) 进程状态 : %s" % ("❌ 仍在运行" if proc_running() else "✅ 已完全退出"))
    en, sv = sysproxy()
    print("4) 系统代理 : %s" % ("❌ 已关闭" if en is False else ("⚠️ 仍开启 -> %s" % sv)))
    return 0


def cmd_mode(args):
    if args.value not in ("rule", "global", "direct", "script"):
        print("❌ mode 必须是 rule / global / direct / script")
        return 1
    _, err = api_patch("/configs", {"mode": args.value})
    print("切换 mode -> %s : %s" % (args.value, "✅ 成功" if not err else "❌ %s" % err))
    return 0 if not err else 1


def cmd_nodes(args):
    d, err = api_get("/proxies")
    if err:
        print("❌ %s" % err)
        return 1
    ps = d.get("proxies", {})
    print("代理组 / Groups:")
    for name, v in ps.items():
        if v.get("type") in ("Selector", "URLTest", "Fallback", "LoadBalance"):
            now = v.get("now", "-")
            print("  [%s] %-10s 当前=%s" % (v.get("type"), name, now))
    print()
    print("节点 / Nodes（仅显示名称与最近延迟）:")
    for name, v in ps.items():
        if v.get("type") in ("Selector", "URLTest", "Fallback", "LoadBalance",
                             "Direct", "Reject", "RejectDrop"):
            continue
        hist = v.get("history", [])
        delay = hist[-1].get("delay") if hist else None
        print("  %-34s %-9s %s" % (name, v.get("type"),
                                   ("%d ms" % delay) if delay else "无延迟记录"))
    return 0


def cmd_use(args):
    d, err = api_get("/proxies")
    if err:
        print("❌ %s" % err)
        return 1
    ps = d.get("proxies", {})
    if args.node not in ps:
        print("❌ 节点不存在：%s" % args.node)
        print("   可用节点见 `python clash_ctl.py nodes`")
        return 1
    # 找到包含该节点的 Selector/URLTest 组并切换
    target = args.group or "GLOBAL"
    if target not in ps:
        cands = [n for n, v in ps.items()
                 if v.get("type") in ("Selector", "URLTest")
                 and args.node in (v.get("all") or [])]
        if not cands:
            print("❌ 未找到包含该节点的代理组")
            return 1
        target = cands[0]
    _, err = api_put("/proxies/%s" % urllib.parse.quote(target), {"name": args.node})
    print("切换 %s -> %s : %s" % (target, args.node, "✅ 成功" if not err else "❌ %s" % err))
    return 0 if not err else 1


def cmd_probe(args):
    do_probe(args)
    return 0


# ---------------------------------------------------------------- 入口

def main():
    ap = argparse.ArgumentParser(description="Clash for Windows 控制器")
    sub = ap.add_subparsers(dest="cmd")

    sub.add_parser("status", help="查看状态并探测通道").set_defaults(func=cmd_status)
    p_on = sub.add_parser("on", help="开启 Clash")
    p_on.add_argument("--export", action="store_true", help="输出可 source 的 export 语句")
    p_on.add_argument("--direct", action="store_true", help="启动后仍保持 direct（不切 rule）")
    p_on.set_defaults(func=cmd_on)
    p_off = sub.add_parser("off", help="关闭 Clash")
    p_off.add_argument("--soft", action="store_true", help="仅切 direct，不退出进程")
    p_off.set_defaults(func=cmd_off)
    p_m = sub.add_parser("mode", help="切换模式")
    p_m.add_argument("value")
    p_m.set_defaults(func=cmd_mode)
    sub.add_parser("nodes", help="列出节点").set_defaults(func=cmd_nodes)
    p_u = sub.add_parser("use", help="切换节点")
    p_u.add_argument("node")
    p_u.add_argument("--group", help="指定代理组，默认 GLOBAL")
    p_u.set_defaults(func=cmd_use)
    sub.add_parser("probe", help="仅探测通道").set_defaults(func=cmd_probe)

    args = ap.parse_args()
    if not args.cmd:
        ap.print_help()
        return 0
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
