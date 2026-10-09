#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
以「完整 profile」启动 Clash 内核（无 GUI）/ Start Clash core with full profile
=============================================================================

### 为什么需要这个脚本

Clash for Windows (CFW) 是 Electron GUI，**在无交互桌面会话中拉不起来**
（实测：直接 Popen/后台启动 `Clash for Windows.exe` 均无效，进程立刻消失）。

而直接跑 `clash-win64.exe -d ~/.config/clash` 也不行：CFW 生成的 `config.yaml`
只有 4 行（mixed-port / allow-lan / external-controller / secret），**没有 proxies 和 rules**，
内核会启动后随即退出，且无法转发任何流量（全部 000）。

真正的订阅配置在 `profiles/<id>.yml`（约 29 KB，含 proxies / proxy-groups / rules）。
本脚本把两者合并后交给内核，从而**脱离 GUI 也能提供完整代理能力**。

### 用法

    python clash_core_start.py            # 合并并启动内核，等待 API 就绪
    python clash_core_start.py --check    # 只检查状态，不启动

### 安全

`secret` 从 `config.yaml` 读取后写入合并配置（内核 API 需要），
**任何输出中均以 *** 遮蔽**，不硬编码、不入代码仓。
"""

import argparse
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import clash_ctl as cc  # noqa: E402

MERGED = os.path.join(cc.USERPROFILE, ".config", "clash", "_merged_cli.yml")


def pick_profile():
    """挑选体积最大（内容最全）的 profile —— 通常就是含订阅节点的那个。"""
    pdir = os.path.join(cc.USERPROFILE, ".config", "clash", "profiles")
    best, best_size = None, 0
    try:
        for fn in os.listdir(pdir):
            if not fn.endswith(".yml"):
                continue
            p = os.path.join(pdir, fn)
            sz = os.path.getsize(p)
            if sz > best_size:
                best, best_size = p, sz
    except FileNotFoundError:
        pass
    return best, best_size


def build_merged(profile, ctrl, secret):
    """把 profile 中的 external-controller / secret 替换成 config.yaml 的值。"""
    with open(profile, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    out, done_ctrl, done_secret = [], False, False
    for ln in lines:
        s = ln.strip()
        if s.startswith("external-controller:"):
            out.append("external-controller: %s" % ctrl)
            done_ctrl = True
        elif s.startswith("secret:"):
            out.append('secret: "%s"' % secret)
            done_secret = True
        else:
            out.append(ln)
    # profile 若缺少这两项则补到末尾（必须在 proxies 之前其实无所谓，clash 解析整个 yaml）
    if not done_ctrl:
        out.append("external-controller: %s" % ctrl)
    if not done_secret:
        out.append('secret: "%s"' % secret)
    with open(MERGED, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    return MERGED


def start_core(cfgdir, merged):
    DETACHED_PROCESS = 0x00000008
    CREATE_NEW_PROCESS_GROUP = 0x00000200
    subprocess.Popen(
        [cc.CLASH_CORE, "-d", cfgdir, "-f", merged],
        stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP, close_fds=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只检查状态")
    ap.add_argument("--wait", type=int, default=40, help="等待 API 就绪秒数")
    args = ap.parse_args()

    cfgdir = os.path.join(cc.USERPROFILE, ".config", "clash")
    ctrl, secret = cc.read_cfg()
    print("配置目录 : %s" % cfgdir)
    print("控制端口 : %s" % (ctrl or "(未读取到)"))
    print("secret   : %s  (遮蔽)" % cc._mask(secret))

    if args.check:
        print("内核进程 : %s" % ("运行中" if cc.proc_running() else "未运行"))
        d, err = cc.api_get("/proxies", timeout=5)
        print("API      : %s" % ("✅ 节点数=%d" % len(d.get("proxies", {})) if not err else "❌ %s" % err))
        return 0

    if not ctrl or not secret:
        print("❌ 无法从 config.yaml 读取 external-controller / secret")
        return 1
    profile, sz = pick_profile()
    if not profile:
        print("❌ 未找到 profile")
        return 1
    print("选用profile: %s (%d bytes)" % (os.path.basename(profile), sz))

    merged = build_merged(profile, ctrl, secret)
    print("合并配置 : %s" % merged)

    if cc.proc_running():
        print("内核已在运行，先结束旧进程 ...")
        subprocess.run(["taskkill", "/F", "/IM", "clash-win64.exe"], capture_output=True)
        time.sleep(2)

    start_core(cfgdir, merged)
    print("等待 API 就绪（最多 %d 秒）..." % args.wait, flush=True)
    for i in range(args.wait):
        time.sleep(1)
        d, err = cc.api_get("/proxies", timeout=3)
        if not err:
            n = len(d.get("proxies", {}))
            print("✅ 内核就绪（%d 秒），代理条目 = %d" % (i + 1, n))
            break
    else:
        print("⚠️ API 未就绪，检查 %s" % os.path.join(cfgdir, "logs"))
        return 1

    # 内核不会自己设系统代理（那是 CFW 的活），这里补上
    en, sv = cc.sysproxy()
    if en is False:
        ok, err = cc.set_sysproxy(True)
        print("系统代理 : %s" % ("✅ 已开启" if ok else "❌ %s" % err))
    else:
        print("系统代理 : ✅ 已开启 -> %s" % sv)
    return 0


if __name__ == "__main__":
    sys.exit(main())
