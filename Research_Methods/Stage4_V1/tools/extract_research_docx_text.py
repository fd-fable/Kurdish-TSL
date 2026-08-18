#!/usr/bin/env python3
"""Mechanical extraction of research DOCX reports for independent audit.

This tool performs NO linguistic interpretation. It exposes paragraph and table
content of committed DSR/LDR/protocol/audit Word files as UTF-8 text/JSONL with
stable mechanical locators and SHA-256 provenance.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Iterator, Tuple

from docx import Document
from docx.document import Document as _Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl

ROOT = Path(__file__).resolve().parents[3]
OUT_ROOT = ROOT / "Research_Extracts" / "Stage4_V1" / "Research_Reports"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def iter_blocks(doc: _Document) -> Iterator[Tuple[str, object]]:
    for child in doc.element.body.iterchildren():
        if isinstance(child, CT_P):
            yield "P", Paragraph(child, doc)
        elif isinstance(child, CT_Tbl):
            yield "T", Table(child, doc)


def clean(text: str) -> str:
    return text.replace("\r", "").replace("\t", " ").strip("\n")


def output_dir_for(path: Path) -> Path:
    rel_parent = path.parent.relative_to(ROOT)
    return OUT_ROOT / rel_parent


def extract(path: Path) -> dict:
    doc = Document(path)
    out_dir = output_dir_for(path)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = path.stem
    txt_path = out_dir / f"{stem}__MECHANICAL_REPORT_EXTRACT.txt"
    jsonl_path = out_dir / f"{stem}__MECHANICAL_REPORT_EXTRACT.jsonl"

    records = []
    p_count = 0
    t_count = 0

    with txt_path.open("w", encoding="utf-8", newline="\n") as tf:
        tf.write("# MECHANICAL RESEARCH-REPORT EXTRACTION ONLY\n")
        tf.write(f"# Source: {path.relative_to(ROOT).as_posix()}\n")
        tf.write(f"# Source SHA256: {sha256(path)}\n")
        tf.write("# No linguistic claim in this extraction is endorsed by the extractor.\n\n")

        for kind, block in iter_blocks(doc):
            if kind == "P":
                p_count += 1
                para: Paragraph = block  # type: ignore[assignment]
                style = para.style.name if para.style is not None else ""
                rec = {
                    "kind": "paragraph",
                    "locator": f"RP{p_count:06d}",
                    "style": style,
                    "text": clean(para.text),
                }
                records.append(rec)
                tf.write(f"[{rec['locator']}] {rec['text']}\n")
            else:
                t_count += 1
                table: Table = block  # type: ignore[assignment]
                for r_idx, row in enumerate(table.rows, start=1):
                    cells = [clean(cell.text) for cell in row.cells]
                    rec = {
                        "kind": "table_row",
                        "locator": f"RT{t_count:04d}-R{r_idx:04d}",
                        "cells": cells,
                    }
                    records.append(rec)
                    tf.write(f"[{rec['locator']}] " + " | ".join(cells) + "\n")

    with jsonl_path.open("w", encoding="utf-8", newline="\n") as jf:
        for rec in records:
            jf.write(json.dumps(rec, ensure_ascii=False) + "\n")

    return {
        "source": path.relative_to(ROOT).as_posix(),
        "sha256": sha256(path),
        "paragraphs": p_count,
        "tables": t_count,
        "records": len(records),
        "text_output": txt_path.relative_to(ROOT).as_posix(),
        "jsonl_output": jsonl_path.relative_to(ROOT).as_posix(),
    }


def selected_docx() -> list[Path]:
    files: list[Path] = []
    for corpus in sorted(p for p in ROOT.iterdir() if p.is_dir() and p.name[:3].isdigit()):
        files.extend(sorted(corpus.glob("DSR*.docx")))
        files.extend(sorted(corpus.glob("LDRSTLK*.docx")))

    for root_name in (
        "TSLK_DISCOVERY_PROTOCOL_V1.docx",
        "TSLK_METHODOLOGICAL_REPLICATION_AUDIT_V1.docx",
    ):
        p = ROOT / root_name
        if p.exists():
            files.append(p)

    # De-duplicate while retaining stable lexical order.
    return sorted(set(files), key=lambda p: p.relative_to(ROOT).as_posix())


def main() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    docs = selected_docx()
    items = [extract(p) for p in docs]
    manifest = OUT_ROOT / "RESEARCH_REPORT_EXTRACTION_MANIFEST.json"
    manifest.write_text(
        json.dumps({"protocol": "TSLK_DISCOVERY_PROTOCOL_V1", "items": items}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Extracted {len(items)} research DOCX files")
    print(manifest.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
