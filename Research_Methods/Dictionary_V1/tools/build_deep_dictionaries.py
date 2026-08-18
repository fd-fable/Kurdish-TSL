#!/usr/bin/env python3
"""Build exhaustive, corpus-specific Kurdish-TSL dictionary evidence packages.

This program is deliberately mechanical. It extracts written text from committed
CSTLK DOCX files, preserves exact surface forms, counts distributions, and writes
reproducible lexical inventories. It MUST NOT assign meanings, grammatical
categories, lemmas, morphemes, or cross-corpus equivalences.

See: Research_Methods/Dictionary_V1/TSLK_DEEP_DICTIONARY_PROTOCOL_V1.md
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import unicodedata
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Optional, Sequence, Tuple
import xml.etree.ElementTree as ET


SCRIPT_VERSION = "TSLK_DEEP_DICTIONARY_BUILDER_V1.0.0"
WORD_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W = f"{{{WORD_NS}}}"
CORPUS_DIR_RE = re.compile(r"^\d{3}_.+")
CSTLK_RE = re.compile(r"^CSTLK.*\.docx$", re.IGNORECASE)

# These characters may occur internally inside a technical word-like span, but
# only when there is a Unicode letter/mark/number immediately on both sides.
INTERNAL_CONNECTORS = {
    "'", "’", "ʼ", "ʻ", "‛", "‘", "-", "‐", "‑", "‒", "–", "_"
}

OCCURRENCE_SHARD_ROWS = 200_000
SAMPLE_LOCATOR_LIMIT = 12
CONTEXT_LIMIT = 500
TOP_NEIGHBOR_LIMIT = 12


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sanitize_one_line(text: str, limit: int = CONTEXT_LIMIT) -> str:
    text = text.replace("\r", " ").replace("\n", " ").replace("\t", " ")
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        return text[: limit - 1] + "…"
    return text


def unicode_name(ch: str) -> str:
    try:
        return unicodedata.name(ch)
    except ValueError:
        return "<UNNAMED>"


def is_core_word_char(ch: str) -> bool:
    if not ch:
        return False
    cat = unicodedata.category(ch)
    return cat.startswith("L") or cat.startswith("M") or cat.startswith("N")


def iter_mechanical_spans(text: str) -> Iterator[Tuple[str, str, int, int]]:
    """Yield (kind, exact_span, start, end) for every non-whitespace char.

    kind WORDLIKE contains Unicode letters/marks/numbers and approved internal
    connectors. kind OTHER contains punctuation/symbol/etc. Every non-whitespace
    source character is assigned to exactly one yielded span.
    """
    i = 0
    n = len(text)
    while i < n:
        if text[i].isspace():
            i += 1
            continue

        if is_core_word_char(text[i]):
            start = i
            i += 1
            while i < n:
                if is_core_word_char(text[i]):
                    i += 1
                    continue
                if (
                    text[i] in INTERNAL_CONNECTORS
                    and i + 1 < n
                    and is_core_word_char(text[i + 1])
                ):
                    i += 1
                    continue
                break
            yield "WORDLIKE", text[start:i], start, i
            continue

        start = i
        i += 1
        while i < n and not text[i].isspace() and not is_core_word_char(text[i]):
            # Stop before a connector that begins an internally connected word
            # only if it is immediately followed by a core char. The connector
            # remains OTHER when it has no core char on its left.
            if text[i] in INTERNAL_CONNECTORS and i + 1 < n and is_core_word_char(text[i + 1]):
                break
            i += 1
        yield "OTHER", text[start:i], start, i


@dataclass
class TextContainer:
    part: str
    locator: str
    text: str


@dataclass
class FormStats:
    frequency: int = 0
    parts: set = field(default_factory=set)
    first_locator: Optional[str] = None
    last_locator: Optional[str] = None
    sample_locators: List[str] = field(default_factory=list)
    first_context: Optional[str] = None
    container_initial_count: int = 0
    container_final_count: int = 0


class DocxTextExtractor:
    """Extract text containers from all relevant text-bearing Word XML parts."""

    def __init__(self, docx_path: Path):
        self.docx_path = docx_path

    @staticmethod
    def _paragraph_text(p: ET.Element) -> str:
        chunks: List[str] = []
        for el in p.iter():
            if el.tag == W + "t":
                chunks.append(el.text or "")
            elif el.tag == W + "tab":
                chunks.append("\t")
            elif el.tag in {W + "br", W + "cr"}:
                chunks.append("\n")
        return "".join(chunks)

    @staticmethod
    def _part_label(name: str) -> str:
        base = Path(name).name
        if name == "word/document.xml":
            return "BODY"
        if base.startswith("header"):
            return "HEADER:" + base
        if base.startswith("footer"):
            return "FOOTER:" + base
        if base == "footnotes.xml":
            return "FOOTNOTE"
        if base == "endnotes.xml":
            return "ENDNOTE"
        if base == "comments.xml":
            return "COMMENT"
        return "WORDXML:" + name.replace("/", ":")

    def iter_containers(self) -> Iterator[TextContainer]:
        with zipfile.ZipFile(self.docx_path, "r") as zf:
            xml_names = sorted(
                n for n in zf.namelist()
                if n.startswith("word/") and n.endswith(".xml")
            )
            # Put document.xml first; other parts sorted deterministically.
            xml_names.sort(key=lambda n: (0 if n == "word/document.xml" else 1, n))

            for name in xml_names:
                data = zf.read(name)
                # Fast filter: avoid parsing styles/settings parts that cannot
                # contribute visible w:t text.
                if b"<w:t" not in data and b":t" not in data:
                    continue
                try:
                    root = ET.fromstring(data)
                except ET.ParseError:
                    continue

                part = self._part_label(name)
                covered_text_nodes = set()
                p_index = 0
                for p in root.iter(W + "p"):
                    p_index += 1
                    text = self._paragraph_text(p)
                    for t in p.iter(W + "t"):
                        covered_text_nodes.add(id(t))
                    if text:
                        yield TextContainer(
                            part=part,
                            locator=f"{part}-P{p_index:06d}",
                            text=text,
                        )

                # Extremely defensive completeness pass: capture any w:t node
                # not contained in an enumerated paragraph.
                orphan_index = 0
                for t in root.iter(W + "t"):
                    if id(t) in covered_text_nodes:
                        continue
                    if t.text:
                        orphan_index += 1
                        yield TextContainer(
                            part=part,
                            locator=f"{part}-ORPHAN{orphan_index:06d}",
                            text=t.text,
                        )


def find_corpus_inputs(repo_root: Path) -> List[Tuple[str, Path]]:
    found: List[Tuple[str, Path]] = []
    for child in sorted(repo_root.iterdir()):
        if not child.is_dir() or not CORPUS_DIR_RE.match(child.name):
            continue
        candidates = [p for p in child.iterdir() if p.is_file() and CSTLK_RE.match(p.name)]
        if not candidates:
            continue
        candidates.sort()
        if len(candidates) > 1:
            print(
                f"WARNING: {child.name} has {len(candidates)} CSTLK candidates; "
                f"using {candidates[0].name} and recording the ambiguity.",
                file=sys.stderr,
            )
        found.append((child.name, candidates[0]))
    return found


def tsv_escape(value) -> str:
    if value is None:
        return ""
    return str(value)


def write_tsv(path: Path, fieldnames: Sequence[str], rows: Iterable[Dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: tsv_escape(row.get(k, "")) for k in fieldnames})


def neighbor_string(counter: Counter, limit: int = TOP_NEIGHBOR_LIMIT) -> str:
    if not counter:
        return ""
    return " | ".join(f"{form}::{count}" for form, count in counter.most_common(limit))


def build_one_dictionary(repo_root: Path, corpus_folder: str, docx_path: Path, out_root: Path, script_hash: str) -> Dict[str, object]:
    out_dir = out_root / corpus_folder
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    source_sha = sha256_file(docx_path)
    extractor = DocxTextExtractor(docx_path)

    form_stats: Dict[str, FormStats] = defaultdict(FormStats)
    raw_counter: Counter = Counter()
    char_counter: Counter = Counter()
    part_container_counter: Counter = Counter()
    left_neighbors: Dict[str, Counter] = defaultdict(Counter)
    right_neighbors: Dict[str, Counter] = defaultdict(Counter)
    casefold_groups: Dict[str, set] = defaultdict(set)

    total_containers = 0
    total_chars = 0
    total_nonspace_chars = 0
    covered_nonspace_chars = 0
    total_wordlike_occurrences = 0
    total_raw_tokens = 0
    total_other_spans = 0

    # Temporary occurrence spool stores exact mechanical evidence without holding
    # millions of occurrence dictionaries in RAM.
    temp_fd, temp_name = tempfile.mkstemp(prefix="tslk_occ_", suffix=".jsonl")
    os.close(temp_fd)
    temp_path = Path(temp_name)

    try:
        with temp_path.open("w", encoding="utf-8") as occ_tmp:
            for container in extractor.iter_containers():
                total_containers += 1
                part_container_counter[container.part] += 1
                text = container.text
                total_chars += len(text)
                char_counter.update(text)
                total_nonspace_chars += sum(1 for ch in text if not ch.isspace())

                raw_tokens = re.findall(r"\S+", text, flags=re.UNICODE)
                raw_counter.update(raw_tokens)
                total_raw_tokens += len(raw_tokens)

                spans = list(iter_mechanical_spans(text))
                covered_nonspace_chars += sum(len(span) for _, span, _, _ in spans)
                total_other_spans += sum(1 for kind, _, _, _ in spans if kind == "OTHER")
                word_spans = [(span, start, end) for kind, span, start, end in spans if kind == "WORDLIKE"]
                word_forms = [x[0] for x in word_spans]

                for idx, (surface, start, end) in enumerate(word_spans, start=1):
                    total_wordlike_occurrences += 1
                    local_locator = f"{container.locator}-W{idx:05d}"
                    st = form_stats[surface]
                    st.frequency += 1
                    st.parts.add(container.part)
                    if st.first_locator is None:
                        st.first_locator = local_locator
                        st.first_context = sanitize_one_line(text)
                    st.last_locator = local_locator
                    if len(st.sample_locators) < SAMPLE_LOCATOR_LIMIT:
                        st.sample_locators.append(local_locator)
                    if idx == 1:
                        st.container_initial_count += 1
                    if idx == len(word_spans):
                        st.container_final_count += 1

                    left1 = word_forms[idx - 2] if idx > 1 else ""
                    right1 = word_forms[idx] if idx < len(word_forms) else ""
                    if left1:
                        left_neighbors[surface][left1] += 1
                    if right1:
                        right_neighbors[surface][right1] += 1

                    nfc = unicodedata.normalize("NFC", surface)
                    cf = nfc.casefold()
                    casefold_groups[cf].add(surface)

                    occ_tmp.write(json.dumps({
                        "surface_form": surface,
                        "locator": local_locator,
                        "document_part": container.part,
                        "container_locator": container.locator,
                        "token_index": idx,
                        "container_wordlike_count": len(word_spans),
                        "left1": left1,
                        "right1": right1,
                        "context": sanitize_one_line(text),
                        "char_start": start,
                        "char_end": end,
                    }, ensure_ascii=False) + "\n")

        coverage_ok = covered_nonspace_chars == total_nonspace_chars
        frequency_sum_ok = sum(st.frequency for st in form_stats.values()) == total_wordlike_occurrences
        raw_frequency_sum_ok = sum(raw_counter.values()) == total_raw_tokens

        # Deterministic entry IDs.
        surfaces = sorted(
            form_stats,
            key=lambda s: (unicodedata.normalize("NFC", s).casefold(), unicodedata.normalize("NFC", s), s),
        )
        entry_id = {surface: f"W{i:06d}" for i, surface in enumerate(surfaces, start=1)}

        raw_forms = sorted(
            raw_counter,
            key=lambda s: (unicodedata.normalize("NFC", s).casefold(), unicodedata.normalize("NFC", s), s),
        )
        raw_id = {surface: f"R{i:06d}" for i, surface in enumerate(raw_forms, start=1)}

        lexicon_fields = [
            "entry_id", "surface_form", "nfc_search_key", "casefold_search_key",
            "frequency", "document_part_count", "document_parts", "first_locator",
            "last_locator", "sample_locators", "first_context", "container_initial_count",
            "container_final_count", "top_left_neighbors", "top_right_neighbors",
            "unicode_char_length", "exact_character_sequence", "first_char", "last_char",
            "first_two_chars", "last_two_chars", "casefold_surface_relatives",
            "semantic_status", "interpretive_status", "corpus_scope_status", "notes",
        ]

        def lexicon_row(surface: str) -> Dict[str, object]:
            st = form_stats[surface]
            nfc = unicodedata.normalize("NFC", surface)
            cf = nfc.casefold()
            relatives = sorted(x for x in casefold_groups[cf] if x != surface)
            return {
                "entry_id": entry_id[surface],
                "surface_form": surface,
                "nfc_search_key": nfc,
                "casefold_search_key": cf,
                "frequency": st.frequency,
                "document_part_count": len(st.parts),
                "document_parts": " | ".join(sorted(st.parts)),
                "first_locator": st.first_locator or "",
                "last_locator": st.last_locator or "",
                "sample_locators": " | ".join(st.sample_locators),
                "first_context": st.first_context or "",
                "container_initial_count": st.container_initial_count,
                "container_final_count": st.container_final_count,
                "top_left_neighbors": neighbor_string(left_neighbors[surface]),
                "top_right_neighbors": neighbor_string(right_neighbors[surface]),
                "unicode_char_length": len(surface),
                "exact_character_sequence": " ".join(surface),
                "first_char": surface[:1],
                "last_char": surface[-1:] if surface else "",
                "first_two_chars": surface[:2],
                "last_two_chars": surface[-2:] if len(surface) >= 2 else surface,
                "casefold_surface_relatives": " | ".join(relatives),
                "semantic_status": "SEMANTIC VALUE UNRESOLVED",
                "interpretive_status": "INTERPRETATION UNREVIEWED",
                "corpus_scope_status": "CORPUS-SCOPE UNREVIEWED",
                "notes": "",
            }

        lexicon_path = out_dir / "LEXICON.tsv"
        write_tsv(lexicon_path, lexicon_fields, (lexicon_row(s) for s in surfaces))

        with (out_dir / "LEXICON.jsonl").open("w", encoding="utf-8") as f:
            for surface in surfaces:
                f.write(json.dumps(lexicon_row(surface), ensure_ascii=False) + "\n")

        raw_fields = [
            "raw_token_id", "raw_token", "frequency", "nfc_search_key",
            "casefold_search_key", "unicode_char_length", "semantic_status",
            "interpretive_status",
        ]
        write_tsv(
            out_dir / "RAW_TOKEN_INVENTORY.tsv",
            raw_fields,
            (
                {
                    "raw_token_id": raw_id[s],
                    "raw_token": s,
                    "frequency": raw_counter[s],
                    "nfc_search_key": unicodedata.normalize("NFC", s),
                    "casefold_search_key": unicodedata.normalize("NFC", s).casefold(),
                    "unicode_char_length": len(s),
                    "semantic_status": "SEMANTIC VALUE UNRESOLVED",
                    "interpretive_status": "INTERPRETATION UNREVIEWED",
                }
                for s in raw_forms
            ),
        )

        char_fields = ["character", "code_point", "unicode_name", "unicode_category", "count"]
        char_rows = []
        for ch, count in sorted(char_counter.items(), key=lambda kv: ord(kv[0])):
            display = ch
            if ch == "\n":
                display = "\\n"
            elif ch == "\r":
                display = "\\r"
            elif ch == "\t":
                display = "\\t"
            elif ch == " ":
                display = "<SPACE>"
            char_rows.append({
                "character": display,
                "code_point": f"U+{ord(ch):04X}",
                "unicode_name": unicode_name(ch),
                "unicode_category": unicodedata.category(ch),
                "count": count,
            })
        write_tsv(out_dir / "CHARACTER_INVENTORY.tsv", char_fields, char_rows)

        # Complete word-like occurrence/concordance stream, gzip-sharded.
        occurrence_fields = [
            "entry_id", "surface_form", "locator", "document_part",
            "container_locator", "token_index", "container_wordlike_count",
            "left1", "right1", "context", "char_start", "char_end",
        ]
        shard_paths: List[str] = []
        shard_index = 0
        shard_rows = 0
        gz = None
        writer = None

        def open_new_shard():
            nonlocal shard_index, shard_rows, gz, writer
            if gz is not None:
                gz.close()
            shard_index += 1
            shard_rows = 0
            shard_name = f"OCCURRENCES_{shard_index:04d}.tsv.gz"
            shard_paths.append(shard_name)
            gz = gzip.open(out_dir / shard_name, "wt", encoding="utf-8", newline="")
            writer = csv.DictWriter(gz, fieldnames=occurrence_fields, delimiter="\t")
            writer.writeheader()

        with temp_path.open("r", encoding="utf-8") as f:
            for line in f:
                if shard_rows == 0 and writer is None:
                    open_new_shard()
                if shard_rows >= OCCURRENCE_SHARD_ROWS:
                    open_new_shard()
                rec = json.loads(line)
                rec["entry_id"] = entry_id[rec["surface_form"]]
                writer.writerow(rec)
                shard_rows += 1
        if gz is not None:
            gz.close()

        corpus_id = corpus_folder.split("_", 1)[0]
        dictionary_status = (
            "MECHANICALLY COMPLETE / INTERPRETATION UNREVIEWED"
            if coverage_ok and frequency_sum_ok and raw_frequency_sum_ok
            else "INCOMPLETE / AUDIT FAILED"
        )

        manifest = {
            "schema": "TSLK_DEEP_DICTIONARY_MANIFEST_V1",
            "builder_version": SCRIPT_VERSION,
            "builder_sha256": script_hash,
            "corpus_folder": corpus_folder,
            "corpus_id": corpus_id,
            "source_cstlk_path": str(docx_path.relative_to(repo_root)).replace(os.sep, "/"),
            "source_cstlk_sha256": source_sha,
            "dictionary_status": dictionary_status,
            "semantic_status": "UNRESOLVED BY MECHANICAL BUILD",
            "counts": {
                "text_containers": total_containers,
                "total_characters": total_chars,
                "non_whitespace_characters": total_nonspace_chars,
                "covered_non_whitespace_characters": covered_nonspace_chars,
                "raw_token_occurrences": total_raw_tokens,
                "raw_token_types": len(raw_counter),
                "wordlike_occurrences": total_wordlike_occurrences,
                "wordlike_surface_types": len(form_stats),
                "other_nonspace_spans": total_other_spans,
                "occurrence_shards": len(shard_paths),
            },
            "document_parts": dict(sorted(part_container_counter.items())),
            "checks": {
                "nonspace_character_coverage_ok": coverage_ok,
                "wordlike_frequency_sum_ok": frequency_sum_ok,
                "raw_frequency_sum_ok": raw_frequency_sum_ok,
                "source_surface_forms_preserved": True,
                "cross_corpus_lemma_merging_performed": False,
                "semantic_assignment_performed": False,
                "grammatical_classification_performed": False,
            },
            "files": {
                "lexicon_tsv": "LEXICON.tsv",
                "lexicon_jsonl": "LEXICON.jsonl",
                "raw_token_inventory": "RAW_TOKEN_INVENTORY.tsv",
                "character_inventory": "CHARACTER_INVENTORY.tsv",
                "occurrence_shards": shard_paths,
                "readme": "README.md",
            },
        }
        with (out_dir / "MANIFEST.json").open("w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2, sort_keys=True)
            f.write("\n")

        readme = f"""# Deep Dictionary — {corpus_folder}

**Status:** {dictionary_status}

**Source CSTLK:** `{manifest['source_cstlk_path']}`  
**Source SHA-256:** `{source_sha}`  
**Builder:** `{SCRIPT_VERSION}`  
**Builder SHA-256:** `{script_hash}`

## Exhaustive inventory

- Layer R raw written-token occurrences: **{total_raw_tokens:,}**
- Layer R distinct raw written-token types: **{len(raw_counter):,}**
- Layer W mechanical word-like occurrences: **{total_wordlike_occurrences:,}**
- Layer W distinct exact surface forms: **{len(form_stats):,}**
- Text containers processed: **{total_containers:,}**
- Non-whitespace character coverage: **{covered_nonspace_chars:,}/{total_nonspace_chars:,}**

## Files

- `LEXICON.tsv` — exhaustive unique Layer W dictionary entries.
- `LEXICON.jsonl` — machine-readable equivalent.
- `RAW_TOKEN_INVENTORY.tsv` — exact whitespace-token inventory preserving punctuation attachment.
- `CHARACTER_INVENTORY.tsv` — complete extracted character inventory.
- `OCCURRENCES_*.tsv.gz` — complete concordance/occurrence stream in shards.
- `MANIFEST.json` — hashes, counts, audit checks, and build provenance.

## Interpretation rule

Every generated entry begins with:

`SEMANTIC VALUE UNRESOLVED`

`INTERPRETATION UNREVIEWED`

`CORPUS-SCOPE UNREVIEWED`

This package does not import external Kurdish meanings, grammar, lemmas, or cross-corpus equivalences. The exact surface form is evidence; technical NFC/casefold fields are search aids only.

## Completeness checks

- Non-whitespace character coverage: **{'PASS' if coverage_ok else 'FAIL'}**
- Layer W frequency sum: **{'PASS' if frequency_sum_ok else 'FAIL'}**
- Layer R frequency sum: **{'PASS' if raw_frequency_sum_ok else 'FAIL'}**

See `Research_Methods/Dictionary_V1/TSLK_DEEP_DICTIONARY_PROTOCOL_V1.md`.
"""
        (out_dir / "README.md").write_text(readme, encoding="utf-8")

        return manifest

    finally:
        try:
            temp_path.unlink(missing_ok=True)
        except Exception:
            pass


def write_project_index(out_root: Path, manifests: List[Dict[str, object]], script_hash: str) -> None:
    out_root.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Kurdish-TSL — Corpus-Specific Deep Dictionaries",
        "",
        "**Method:** `Research_Methods/Dictionary_V1/TSLK_DEEP_DICTIONARY_PROTOCOL_V1.md`",
        "",
        "These dictionaries are isolated corpus inventories. This index does not merge forms or meanings across corpora.",
        "",
        "| Corpus | Layer W surface types | Layer W occurrences | Raw token types | Status |",
        "|---|---:|---:|---:|---|",
    ]
    for m in manifests:
        c = m["counts"]
        lines.append(
            f"| `{m['corpus_folder']}` | {c['wordlike_surface_types']:,} | "
            f"{c['wordlike_occurrences']:,} | {c['raw_token_types']:,} | {m['dictionary_status']} |"
        )
    lines.extend([
        "",
        "## Research caution",
        "",
        "A dictionary entry proves only that the exact written form is attested in the committed CSTLK representation under the documented mechanical extraction/tokenization rules. Meaning, pronunciation, lemma identity, grammatical category, morphology, and cross-corpus identity remain separate research questions.",
        "",
    ])
    (out_root / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")

    master = {
        "schema": "TSLK_DEEP_DICTIONARY_MASTER_MANIFEST_V1",
        "builder_version": SCRIPT_VERSION,
        "builder_sha256": script_hash,
        "corpus_count": len(manifests),
        "corpora": manifests,
    }
    (out_root / "DICTIONARY_BUILD_MANIFEST.json").write_text(
        json.dumps(master, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".", help="Repository root")
    parser.add_argument("--output-root", default="Dictionaries", help="Dictionary output directory")
    parser.add_argument("--corpus", action="append", default=[], help="Optional corpus folder(s) to build")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    out_root = (repo_root / args.output_root).resolve()
    script_path = Path(__file__).resolve()
    script_hash = sha256_file(script_path)

    inputs = find_corpus_inputs(repo_root)
    if args.corpus:
        wanted = set(args.corpus)
        inputs = [x for x in inputs if x[0] in wanted]

    if not inputs:
        print("No CSTLK corpus inputs found.", file=sys.stderr)
        return 2

    manifests: List[Dict[str, object]] = []
    for corpus_folder, docx_path in inputs:
        print(f"BUILD {corpus_folder}: {docx_path.name}", flush=True)
        manifest = build_one_dictionary(repo_root, corpus_folder, docx_path, out_root, script_hash)
        manifests.append(manifest)
        c = manifest["counts"]
        print(
            f"  -> {c['wordlike_surface_types']} surface forms / "
            f"{c['wordlike_occurrences']} occurrences / {manifest['dictionary_status']}",
            flush=True,
        )

    write_project_index(out_root, manifests, script_hash)

    failed = [m for m in manifests if not str(m["dictionary_status"]).startswith("MECHANICALLY COMPLETE")]
    if failed:
        print("One or more dictionary builds failed completeness checks:", file=sys.stderr)
        for m in failed:
            print(f" - {m['corpus_folder']}: {m['dictionary_status']}", file=sys.stderr)
        return 3

    print(f"Built {len(manifests)} corpus-specific deep dictionary packages under {out_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
