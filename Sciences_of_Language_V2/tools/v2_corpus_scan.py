#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TECHNICAL_MARKERS = {"http", "https", "www", "com", "org", "net", "html", "htm", "pdf"}
FAMILY_VALIDATION_LIMIT = 10000


def is_letter_no_numeric(s: str) -> bool:
    cats = [unicodedata.category(ch) for ch in s]
    return any(c.startswith("L") for c in cats) and not any(c.startswith("N") for c in cats)


def load_template_risk(root: Path) -> set[str]:
    p = root / "Comparative_Research_V1" / "Data" / "LETTER_BEARING_CROSS_SOURCE_INDEX.tsv.gz"
    out: set[str] = set()
    if not p.exists():
        return out
    with gzip.open(p, "rt", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r.get("repeated_context_template_risk") == "YES":
                form = r.get("surface_form", "")
                if form:
                    out.add(form)
    return out


def active_form(form: str, template_risk: set[str]) -> bool:
    return (
        bool(form)
        and is_letter_no_numeric(form)
        and form not in template_risk
        and form.casefold() not in TECHNICAL_MARKERS
    )


def load_manifest(root: Path, corpus: str) -> dict:
    return json.loads((root / "Dictionaries" / corpus / "MANIFEST.json").read_text(encoding="utf-8"))


def load_v1_family_pairs(root: Path, limit: int = FAMILY_VALIDATION_LIMIT):
    p = root / "Sciences_of_Language_V1" / "Data" / "FORM_FAMILY_CANDIDATES.tsv.gz"
    pairs = []
    targets = set()
    if not p.exists():
        return pairs, targets
    with gzip.open(p, "rt", encoding="utf-8", newline="") as f:
        for i, r in enumerate(csv.DictReader(f, delimiter="\t")):
            if i >= limit:
                break
            base = r.get("base_form", "")
            ext = r.get("extended_form", "")
            if not base or not ext:
                continue
            pairs.append({
                "base": base,
                "extended": ext,
                "edge_side": r.get("edge_side", ""),
                "material": r.get("added_edge_material", ""),
                "v1_score": r.get("form_family_evidence_score", ""),
            })
            targets.add(base); targets.add(ext)
    return pairs, targets


def iter_occurrences(root: Path, corpus: str):
    files = sorted((root / "Dictionaries" / corpus / "Occurrences").glob("OCCURRENCES_*.tsv.gz"))
    if not files:
        raise SystemExit(f"No occurrence shards for {corpus}")
    expected_header = None
    for p in files:
        with gzip.open(p, "rt", encoding="utf-8", newline="") as f:
            header_line = f.readline().rstrip("\n\r")
            header = header_line.split("\t")
            if expected_header is None:
                expected_header = header
            elif header != expected_header:
                raise SystemExit(f"Occurrence header mismatch in {p}")
            idx = {name: i for i, name in enumerate(header)}
            req = ["surface_form", "container_locator", "token_index", "container_wordlike_count", "left1", "right1"]
            missing = [x for x in req if x not in idx]
            if missing:
                raise SystemExit(f"Missing fields {missing} in {p}")
            for line in f:
                parts = line.rstrip("\n\r").split("\t")
                if len(parts) < len(header):
                    parts += [""] * (len(header) - len(parts))
                yield {
                    "surface": parts[idx["surface_form"]],
                    "container": parts[idx["container_locator"]],
                    "token_index": int(parts[idx["token_index"]] or 0),
                    "container_count": int(parts[idx["container_wordlike_count"]] or 0),
                    "left1": parts[idx["left1"]],
                    "right1": parts[idx["right1"]],
                }


def iter_containers(root: Path, corpus: str, template_risk: set[str], audit=None):
    current = None
    rows = []
    last_idx = 0
    for r in iter_occurrences(root, corpus):
        if current is None:
            current = r["container"]
        if r["container"] != current:
            if rows:
                yield current, rows
            current = r["container"]
            rows = []
            last_idx = 0
        if audit is not None:
            audit["scanned_occurrences"] += 1
            if r["token_index"] <= last_idx:
                audit["ordering_anomalies"] += 1
        last_idx = r["token_index"]
        r["active"] = active_form(r["surface"], template_risk)
        if audit is not None:
            if r["active"]:
                audit["candidate_occurrences"] += 1
            else:
                audit["documentary_only_occurrences"] += 1
        rows.append(r)
    if rows:
        yield current, rows


def active_runs(rows):
    run = []
    for r in rows:
        if r["active"]:
            run.append(r["surface"])
        else:
            if run:
                yield run
                run = []
    if run:
        yield run


def emit_windows(root: Path, corpus: str, template_risk: set[str], kind: str):
    for _, rows in iter_containers(root, corpus, template_risk):
        for run in active_runs(rows):
            if kind == "bigram":
                n = 2
                for i in range(len(run)-n+1): print("\t".join(run[i:i+n]))
            elif kind == "trigram":
                n = 3
                for i in range(len(run)-n+1): print("\t".join(run[i:i+n]))
            elif kind == "fourgram":
                n = 4
                for i in range(len(run)-n+1): print("\t".join(run[i:i+n]))
            elif kind == "slot":
                for i in range(len(run)-2):
                    print("\t".join((run[i], run[i+2], run[i+1])))
            elif kind == "gap2":
                for i in range(len(run)-3): print("\t".join((run[i], run[i+3])))
            elif kind == "gap3":
                for i in range(len(run)-4): print("\t".join((run[i], run[i+4])))
            else:
                raise SystemExit(f"Unknown emit kind: {kind}")


def weighted_jaccard(a: Counter, b: Counter) -> float:
    if not a and not b:
        return 0.0
    keys = set(a) | set(b)
    num = sum(min(a[k], b[k]) for k in keys)
    den = sum(max(a[k], b[k]) for k in keys)
    return num / den if den else 0.0


def entropy_norm_counts(vals) -> float:
    vals = [v for v in vals if v > 0]
    if len(vals) <= 1:
        return 0.0
    total = sum(vals)
    h = -sum((v/total)*math.log(v/total) for v in vals)
    return h / math.log(len(vals))


def audit_and_positions(root: Path, corpus: str, out_dir: Path, template_risk: set[str]):
    manifest = load_manifest(root, corpus)
    expected = int(manifest["counts"]["wordlike_occurrences"])
    fam_pairs, targets = load_v1_family_pairs(root)
    context_left = defaultdict(Counter)
    context_right = defaultdict(Counter)
    target_freq = Counter()
    pos = defaultdict(lambda: [0]*10)
    init = Counter(); final = Counter(); active_freq = Counter()
    audit = {
        "schema": "TSLK_SCIENCES_OF_LANGUAGE_V2_CORPUS_AUDIT",
        "corpus": corpus,
        "expected_occurrences": expected,
        "scanned_occurrences": 0,
        "candidate_occurrences": 0,
        "documentary_only_occurrences": 0,
        "containers": 0,
        "active_runs": 0,
        "ordering_anomalies": 0,
        "family_validation_limit": FAMILY_VALIDATION_LIMIT,
    }
    for _, rows in iter_containers(root, corpus, template_risk, audit):
        audit["containers"] += 1
        active_rows = [r for r in rows if r["active"]]
        if active_rows:
            init[active_rows[0]["surface"]] += 1
            final[active_rows[-1]["surface"]] += 1
            n = len(active_rows)
            for j, r in enumerate(active_rows):
                form = r["surface"]
                active_freq[form] += 1
                dec = min(9, int((j / max(1, n)) * 10))
                pos[form][dec] += 1
        for run in active_runs(rows):
            audit["active_runs"] += 1
        for r in rows:
            form = r["surface"]
            if form not in targets:
                continue
            target_freq[form] += 1
            l = r["left1"]; rr = r["right1"]
            if active_form(l, template_risk): context_left[form][l] += 1
            if active_form(rr, template_risk): context_right[form][rr] += 1

    audit["coverage_pass"] = audit["scanned_occurrences"] == expected
    audit["ordering_pass"] = audit["ordering_anomalies"] == 0
    if not audit["coverage_pass"]:
        raise SystemExit(f"Coverage mismatch for {corpus}: {audit['scanned_occurrences']} != {expected}")

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "CORPUS_AUDIT.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2, sort_keys=True)+"\n", encoding="utf-8")

    with gzip.open(out_dir / "POSITION_PROFILES.tsv.gz", "wt", encoding="utf-8", newline="") as f:
        fields = ["surface_form","frequency","initial_count","final_count"] + [f"decile_{i}" for i in range(10)]
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
        w.writeheader()
        for form, freq in sorted(active_freq.items(), key=lambda x:(-x[1], x[0].casefold(), x[0])):
            r = {"surface_form":form,"frequency":freq,"initial_count":init[form],"final_count":final[form]}
            for i,v in enumerate(pos[form]): r[f"decile_{i}"] = v
            w.writerow(r)

    with gzip.open(out_dir / "MORPH_CONTEXT_PAIR_EVIDENCE.tsv.gz", "wt", encoding="utf-8", newline="") as f:
        fields = ["base_form","extended_form","edge_side","added_edge_material","v1_score","base_frequency","extended_frequency","left_context_weighted_jaccard","right_context_weighted_jaccard","combined_context_similarity","status"]
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
        w.writeheader()
        for p in fam_pairs:
            b,e = p["base"],p["extended"]
            if target_freq[b] == 0 or target_freq[e] == 0:
                continue
            lj = weighted_jaccard(context_left[b], context_left[e])
            rj = weighted_jaccard(context_right[b], context_right[e])
            w.writerow({
                "base_form":b,"extended_form":e,"edge_side":p["edge_side"],"added_edge_material":p["material"],"v1_score":p["v1_score"],
                "base_frequency":target_freq[b],"extended_frequency":target_freq[e],
                "left_context_weighted_jaccard":f"{lj:.8f}","right_context_weighted_jaccard":f"{rj:.8f}",
                "combined_context_similarity":f"{(lj+rj)/2:.8f}",
                "status":"V1 FORM-FAMILY CANDIDATE / FULL-OCCURRENCE CONTEXT TEST / FUNCTION UNRESOLVED"
            })
    return audit


def format_counts(kind: str, min_count: int):
    headers = {
        "bigram":["support","form_1","form_2"],
        "trigram":["support","form_1","form_2","form_3"],
        "fourgram":["support","form_1","form_2","form_3","form_4"],
        "gap2":["support","left_form","right_form"],
        "gap3":["support","left_form","right_form"],
    }
    fields = headers[kind]
    print("\t".join(fields))
    rx = re.compile(r"^\s*(\d+)\s(.*)$")
    for line in sys.stdin:
        m = rx.match(line.rstrip("\n"))
        if not m: continue
        count = int(m.group(1))
        if count < min_count: continue
        pat = m.group(2)
        print(f"{count}\t{pat}")


def format_slot(min_support: int = 3, min_fillers: int = 2):
    print("left_form\tright_form\ttotal_support\tdistinct_fillers\tfiller_entropy\ttop_fillers\tstatus")
    rx = re.compile(r"^\s*(\d+)\s(.*)$")
    current = None
    support = 0
    fillers = Counter()
    def flush():
        nonlocal current,support,fillers
        if current is None or support < min_support or len(fillers) < min_fillers:
            return
        ent = entropy_norm_counts(fillers.values())
        top = " | ".join(f"{x}::{n}" for x,n in fillers.most_common(20))
        print(f"{current[0]}\t{current[1]}\t{support}\t{len(fillers)}\t{ent:.8f}\t{top}\tVARIABLE-SLOT FRAME CANDIDATE / FUNCTION UNRESOLVED")
    for line in sys.stdin:
        m=rx.match(line.rstrip("\n"))
        if not m: continue
        count=int(m.group(1)); parts=m.group(2).split("\t")
        if len(parts)!=3: continue
        key=(parts[0],parts[1]); filler=parts[2]
        if current is not None and key != current:
            flush(); support=0; fillers=Counter()
        current=key; support += count; fillers[filler] += count
    flush()


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--corpus")
    ap.add_argument("--out-dir")
    ap.add_argument("--mode", required=True, choices=["audit","emit-bigram","emit-trigram","emit-fourgram","emit-slot","emit-gap2","emit-gap3","format-counts","format-slot"])
    ap.add_argument("--kind", choices=["bigram","trigram","fourgram","gap2","gap3"])
    ap.add_argument("--min-count", type=int, default=2)
    args=ap.parse_args()
    root=Path(args.repo_root).resolve()
    if args.mode == "format-counts":
        if not args.kind: raise SystemExit("--kind required")
        return format_counts(args.kind,args.min_count)
    if args.mode == "format-slot":
        return format_slot()
    if not args.corpus: raise SystemExit("--corpus required")
    risk=load_template_risk(root)
    if args.mode == "audit":
        out=Path(args.out_dir) if args.out_dir else root/"Sciences_of_Language_V2"/"Per_Source"/args.corpus
        audit=audit_and_positions(root,args.corpus,out,risk)
        print(json.dumps(audit,ensure_ascii=False,sort_keys=True))
        return
    kind=args.mode.removeprefix("emit-")
    emit_windows(root,args.corpus,risk,kind)

if __name__ == "__main__":
    main()
