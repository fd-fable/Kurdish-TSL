#!/usr/bin/env python3
"""Mechanical extraction of committed CSTLK DOCX corpora.

This tool performs NO linguistic analysis. It preserves document order as far as
python-docx exposes block items and writes paragraph/table text with stable
mechanical locators for later direct AI inspection.

Outputs are stored under Research_Extracts/Stage4_V1/<corpus>/.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Iterable, Iterator, Tuple

from docx import Document
from docx.document import Document as _Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl

ROOT = Path(__file__).resolve().parents[3]
OUT_ROOT = ROOT / "Research_Extracts" / "Stage4_V1"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def iter_block_items(parent: _Document) -> Iterator[Tuple[str, object]]:
    """Yield paragraphs and tables in document order."""
    parent_elm = parent.element.body
    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield "P", Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield "T", Table(child, parent)


def clean_text(text: str) -> str:
    # Preserve Unicode/graphemes. Normalize only newline/tab control layout.
    return text.replace("\r", "").replace("\t", " ").strip("\n")


def extract_docx(docx_path: Path, corpus_dir: Path) -> dict:
    doc = Document(docx_path)
    out_dir = OUT_ROOT / corpus_dir.name
    out_dir.mkdir(parents=True, exist_ok=True)

    txt_path = out_dir / f"{docx_path.stem}__MECHANICAL_EXTRACT.txt"
    jsonl_path = out_dir / f"{docx_path.stem}__MECHANICAL_EXTRACT.jsonl"

    records = []
    p_idx = 0
    t_idx = 0

    with txt_path.open("w", encoding="utf-8", newline="\n") as txt:
        txt.write(f"# MECHANICAL EXTRACTION ONLY\n")
        txt.write(f"# Source: {docx_path.relative_to(ROOT).as_posix()}\n")
        txt.write(f"# Source SHA256: {sha256(docx_path)}\n")
        txt.write("# No normalization, translation, segmentation, or linguistic classification was performed.\n\n")

        for kind, block in iter_block_items(doc):
            if kind == "P":
                p_idx += 1
                paragraph: Paragraph = block  # type: ignore[assignment]
                text = clean_text(paragraph.text)
                style = paragraph.style.name if paragraph.style is not None else ""
                rec = {
                    "kind": "paragraph",
                    "locator": f"P{p_idx:06d}",
                    "style": style,
                    "text": text,
                }
                records.append(rec)
                txt.write(f"[{rec['locator']}] {text}\n")
            else:
                t_idx += 1
                table: Table = block  # type: ignore[assignment]
                for r_idx, row in enumerate(table.rows, start=1):
                    cells = [clean_text(cell.text) for cell in row.cells]
                    locator = f"T{t_idx:04d}-R{r_idx:04d}"
                    rec = {
                        "kind": "table_row",
                        "locator": locator,
                        "cells": cells,
                    }
                    records.append(rec)
                    txt.write(f"[{locator}] " + " | ".join(cells) + "\n")

    with jsonl_path.open("w", encoding="utf-8", newline="\n") as jf:
        for rec in records:
            jf.write(json.dumps(rec, ensure_ascii=False) + "\n")

    return {
        "corpus": corpus_dir.name,
        "source": docx_path.relative_to(ROOT).as_posix(),
        "source_sha256": sha256(docx_path),
        "paragraphs": p_idx,
        "tables": t_idx,
        "records": len(records),
        "text_output": txt_path.relative_to(ROOT).as_posix(),
        "jsonl_output": jsonl_path.relative_to(ROOT).as_posix(),
    }


def main() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    manifest = []

    corpus_dirs = sorted(
        p for p in ROOT.iterdir()
        if p.is_dir() and len(p.name) >= 4 and p.name[:3].isdigit() and p.name[3] == "_"
    )

    for corpus_dir in corpus_dirs:
        docx_files = sorted(corpus_dir.glob("CSTLK*.docx"))
        for docx_path in docx_files:
            manifest.append(extract_docx(docx_path, corpus_dir))

    manifest_path = OUT_ROOT / "MECHANICAL_EXTRACTION_MANIFEST.json"
    manifest_path.write_text(
        json.dumps({"protocol": "TSLK_DISCOVERY_PROTOCOL_V1", "items": manifest}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Extracted {len(manifest)} CSTLK documents")
    print(manifest_path.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
