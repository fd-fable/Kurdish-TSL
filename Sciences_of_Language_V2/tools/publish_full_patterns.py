#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import shutil
from pathlib import Path

SOURCES = [
    "001_MEM_U_ZIN",
    "002_ANHA",
    "003_RONAHI",
    "004_RUDAW",
    "005_PIRTUKEN_KURMANCI_KATALOG",
    "006_KURMANJI_BEGINNERS",
    "007_KOVARA_KURMANCI",
    "008_KOVARA_HAWAR",
    "009_ROJNAMA_KURDISTAN",
    "010_KOVARA_JIN",
    "011_FOLKLORA_KURMANCA_1936",
    "012_KURD_TEAVUN_TERAKKI_1908",
    "013_ROJI_KURD_1913",
    "014_DIROK_U_CIVAKA_KURDAN",
]
KINDS = ["BIGRAMS", "TRIGRAMS", "FOURGRAMS", "SLOT_FRAMES", "GAP2", "GAP3"]
MAX_GIT_FILE_BYTES = 95 * 1024 * 1024


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def count_gz_tsv_rows(path: Path) -> int:
    count = 0
    with gzip.open(path, "rt", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        try:
            next(reader)
        except StopIteration:
            return 0
        for _ in reader:
            count += 1
    return count


def append_once(path: Path, marker: str, block: str) -> None:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    if marker not in text:
        if text and not text.endswith("\n"):
            text += "\n"
        text += "\n" + block.strip() + "\n"
        path.write_text(text, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifacts-root", required=True)
    ap.add_argument("--output-root", default="Sciences_of_Language_V2")
    args = ap.parse_args()

    artifacts = Path(args.artifacts_root).resolve()
    out = Path(args.output_root).resolve()
    master = {
        "schema": "TSLK_SCIENCES_OF_LANGUAGE_V2_FULL_PATTERN_REPOSITORY_MANIFEST",
        "source_count": len(SOURCES),
        "pattern_kinds_per_source": len(KINDS),
        "expected_full_pattern_tables": len(SOURCES) * len(KINDS),
        "tables": [],
    }

    for corpus in SOURCES:
        src_dir = artifacts / "Per_Source" / corpus / "Patterns"
        dst_dir = out / "Per_Source" / corpus / "Patterns"
        dst_dir.mkdir(parents=True, exist_ok=True)
        source_manifest = {
            "corpus": corpus,
            "expected_tables": len(KINDS),
            "tables": [],
        }
        for kind in KINDS:
            src = src_dir / f"{kind}.tsv.gz"
            if not src.exists():
                raise SystemExit(f"Missing complete pattern table: {src}")
            # Full gzip integrity pass before publication.
            rows = count_gz_tsv_rows(src)
            size = src.stat().st_size
            if size > MAX_GIT_FILE_BYTES:
                raise SystemExit(
                    f"Pattern table exceeds Git-safe publication threshold ({MAX_GIT_FILE_BYTES}): {src} ({size})"
                )
            dst = dst_dir / src.name
            shutil.copy2(src, dst)
            digest = sha256(dst)
            rec = {
                "kind": kind,
                "path": str(dst.relative_to(out.parent)).replace("\\", "/"),
                "rows": rows,
                "compressed_bytes": size,
                "sha256": digest,
                "gzip_integrity": "PASS",
            }
            source_manifest["tables"].append(rec)
            master["tables"].append({"corpus": corpus, **rec})

        source_manifest["published_table_count"] = len(source_manifest["tables"])
        source_manifest["complete"] = source_manifest["published_table_count"] == len(KINDS)
        (out / "Per_Source" / corpus / "FULL_PATTERN_MANIFEST.json").write_text(
            json.dumps(source_manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    master["published_full_pattern_tables"] = len(master["tables"])
    master["complete"] = master["published_full_pattern_tables"] == master["expected_full_pattern_tables"]
    master["storage"] = "DIRECT_GIT_REPOSITORY"
    master["actions_artifacts_required_for_future_access"] = False
    if not master["complete"]:
        raise SystemExit("Full per-source pattern publication incomplete")

    (out / "FULL_PATTERN_REPOSITORY_MANIFEST.json").write_text(
        json.dumps(master, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    manifest_path = out / "SCIENCES_OF_LANGUAGE_V2_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["per_source_full_pattern_tables_storage"] = "DIRECT_GIT_REPOSITORY"
    manifest["per_source_full_pattern_tables_committed"] = True
    manifest["per_source_full_pattern_table_count"] = master["published_full_pattern_tables"]
    manifest["full_pattern_repository_manifest"] = "Sciences_of_Language_V2/FULL_PATTERN_REPOSITORY_MANIFEST.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    marker = "## Full per-source pattern evidence in GitHub"
    block = f"""
{marker}

All complete source-local V2 recurrent-pattern tables are repository-resident under
`Per_Source/<CORPUS>/Patterns/`. This includes all six pattern families for all fourteen
sources: BIGRAMS, TRIGRAMS, FOURGRAMS, SLOT_FRAMES, GAP2, and GAP3.

- Complete tables committed: **{master['published_full_pattern_tables']}/{master['expected_full_pattern_tables']}**.
- Every compressed table passed a full gzip read/integrity check before publication.
- Every table has a SHA-256 digest, compressed byte size, and exact data-row count in
  `FULL_PATTERN_REPOSITORY_MANIFEST.json` and the source-local `FULL_PATTERN_MANIFEST.json`.
- GitHub Actions artifacts are backup/build transport only; they are not required to access the full V2 evidence.
"""
    append_once(out / "README.md", marker, block)
    append_once(out / "TSLK_SCIENCES_OF_LANGUAGE_REPORT_V2.md", marker, block)

    audit_path = out / "TSLK_SCIENCES_OF_LANGUAGE_AUDIT_V2.md"
    append_once(
        audit_path,
        "## Repository-resident full-pattern audit",
        f"""
## Repository-resident full-pattern audit

- Expected complete source-local pattern tables: **{master['expected_full_pattern_tables']}**
- Published complete source-local pattern tables: **{master['published_full_pattern_tables']}**
- All gzip integrity checks: **PASS**
- All files below 95 MiB Git publication threshold: **PASS**
- Direct Git repository storage: **PASS**
""",
    )

    print(json.dumps({
        "complete": master["complete"],
        "published_full_pattern_tables": master["published_full_pattern_tables"],
        "expected_full_pattern_tables": master["expected_full_pattern_tables"],
        "storage": master["storage"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
