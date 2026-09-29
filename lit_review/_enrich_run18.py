#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossref + Unpaywall enrichment for new_records of run #18."""
import json, re, sys, time, urllib.parse, urllib.request

PATH = "search_results_20260814_025551.json"
MAIL = "lit-review@local"
TIMEOUT = 40

def http_json(url, retries=2):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": f"lit-review (mailto:{MAIL})", "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            last = e
            time.sleep(1.5*(i+1))
    return {"__error__": str(last)}

def main():
    data = json.load(open(PATH, encoding="utf-8"))
    nr = data["new_records"]
    print(f"=== NEW RECORDS: {len(nr)} ===\n")
    for r in nr:
        print("-"*70)
        print(f"[{r['relevance']}] {'/'.join(r['dimension_labels'])} "
              f"{'[preprint]' if r['is_preprint'] else ''}")
        print(f"DATE: {r['publication_date']}")
        print(f"TITLE: {r['title']}")
        print(f"DOI: {r['doi'] or '-'}  PMID: {r['pmid'] or '待编目'}")
        print(f"VENUE: {r.get('venue')}  OA: {r.get('oa_status')}")
        ab = (r.get('abstract') or '')
        print(f"ABSTRACT({len(ab)}c): {ab[:600]}")
        # Crossref
        if r.get('doi'):
            cj = http_json(f"https://api.crossref.org/works/{urllib.parse.quote(r['doi'])}")
            if 'message' in cj:
                m = cj['message']
                cr_title = (m.get('title') or [''])[0]
                print(f"  CROSSREF title: {cr_title[:90]}")
                print(f"  CROSSREF type: {m.get('type')} | container: {(m.get('container-title') or [''])[0]}")
                print(f"  CROSSREF issued: {m.get('issued')}")
            else:
                print(f"  CROSSREF err: {cj.get('__error__')}")
            # Unpaywall
            uj = http_json(f"https://api.unpaywall.org/api/v2/doi/{urllib.parse.quote(r['doi'])}?email={MAIL}")
            if 'best_oa_location' in uj:
                loc = uj.get('best_oa_location') or {}
                print(f"  UNPAYWALL oa_status: {uj.get('oa_status')} | pdf: {loc.get('pdf_url')}")
            else:
                print(f"  UNPAYWALL err: {uj.get('__error__')}")
        time.sleep(0.3)
    # also print summary
    print("\n=== SUMMARY ===")
    print(json.dumps(data['summary'], ensure_ascii=False, indent=2))

main()
