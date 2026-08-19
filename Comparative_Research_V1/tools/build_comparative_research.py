#!/usr/bin/env python3
"""Build the Kurdish-TSL cross-source comparative research layer.

This script does not assign meanings, lemmas, grammatical categories, or
pronunciations. It compares the already committed corpus-specific Deep
Dictionary V1 evidence packages while preserving source identity.
"""
from __future__ import annotations

import csv
import gzip
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DICT_ROOT = ROOT / "Dictionaries"
OUT = ROOT / "Comparative_Research_V1"

SOURCES = [
    ("001_MEM_U_ZIN", "Mem û Zîn"),
    ("002_ANHA", "ANHA"),
    ("003_RONAHI", "Ronahî"),
    ("004_RUDAW", "Rudaw"),
    ("005_PIRTUKEN_KURMANCI_KATALOG", "Pirtûkên Kurmancî Katalog"),
    ("006_KURMANJI_BEGINNERS", "Kurmanji Beginners"),
    ("007_KOVARA_KURMANCI", "Kovara Kurmancî"),
    ("008_KOVARA_HAWAR", "Kovara Hawar"),
    ("009_ROJNAMA_KURDISTAN", "Rojnama Kurdistan"),
    ("010_KOVARA_JIN", "Kovara Jîn"),
    ("011_FOLKLORA_KURMANCA_1936", "Folklora Kurmanca (1936)"),
    ("012_KURD_TEAVUN_TERAKKI_1908", "Kurd Teavun Terakki (1908)"),
    ("013_ROJI_KURD_1913", "Rojî Kurd (1913)"),
    ("014_DIROK_U_CIVAKA_KURDAN", "Dîrok û Civaka Kurdan"),
]
DISPLAY = dict(SOURCES)


def read_manifest(folder: str) -> dict:
    return json.loads((DICT_ROOT / folder / "MANIFEST.json").read_text(encoding="utf-8"))


def lexicon_files(folder: str):
    d = DICT_ROOT / folder
    files = sorted(d.glob("LEXICON_*.tsv"))
    if not files and (d / "LEXICON.tsv").exists():
        files = [d / "LEXICON.tsv"]
    return files


def load_forms(folder: str):
    freq = Counter()
    for path in lexicon_files(folder):
        with path.open("r", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                form = row.get("surface_form", "")
                if not form:
                    continue
                try:
                    n = int(row.get("frequency", "0") or 0)
                except ValueError:
                    n = 0
                freq[form] += n
    return freq


def md_escape(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", " ")


def pct(n: int, d: int) -> str:
    return "0.00%" if not d else f"{100*n/d:.2f}%"


def list_research_artifacts(folder: str):
    d = ROOT / folder
    items = []
    if not d.exists():
        return items
    for p in sorted(d.iterdir()):
        if p.is_dir() and p.name == "Sources":
            items.append((str(p.relative_to(ROOT)), "PRIMARY SOURCE MATERIAL"))
        elif p.is_file() and p.name.startswith("CSTLK"):
            items.append((str(p.relative_to(ROOT)), "CORPUS EVIDENCE"))
        elif p.is_file() and p.name.startswith("LDRSTLK"):
            items.append((str(p.relative_to(ROOT)), "PRELIMINARY ANALYSIS"))
        elif p.is_file() and (p.name.startswith("DSRSLK") or p.name.startswith("Stage_4_")):
            items.append((str(p.relative_to(ROOT)), "PRESERVED / NOT ACTIVE PROOF AFTER INDEPENDENT STAGE-4 AUDIT"))
    items.append((f"Dictionaries/{folder}/", "ACTIVE MECHANICAL DICTIONARY EVIDENCE"))
    return items


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "Data").mkdir(exist_ok=True)

    manifests = {f: read_manifest(f) for f, _ in SOURCES}
    freqs = {f: load_forms(f) for f, _ in SOURCES}
    sets = {f: set(freqs[f]) for f, _ in SOURCES}

    membership = defaultdict(list)
    global_frequency = Counter()
    for folder, _ in SOURCES:
        for form, n in freqs[folder].items():
            membership[form].append(folder)
            global_frequency[form] += n

    incidence = Counter(len(v) for v in membership.values())
    global_union = len(membership)
    shared_2plus = sum(c for k, c in incidence.items() if k >= 2)
    shared_all = incidence.get(len(SOURCES), 0)

    # Cross-source exact surface index: exhaustive and non-destructive.
    index_path = OUT / "Data" / "EXACT_SURFACE_CROSS_SOURCE_INDEX.tsv.gz"
    with gzip.open(index_path, "wt", encoding="utf-8", newline="") as gz:
        fields = ["surface_form", "source_count", "sources", "global_occurrence_frequency"]
        writer = csv.DictWriter(gz, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for form in sorted(membership, key=lambda x: (x.casefold(), x)):
            folders = membership[form]
            writer.writerow({
                "surface_form": form,
                "source_count": len(folders),
                "sources": " | ".join(f"{DISPLAY[f]} [{f[:3]}]" for f in folders),
                "global_occurrence_frequency": global_frequency[form],
            })

    # Pairwise comparison matrix.
    pair_rows = []
    for i, (a, aname) in enumerate(SOURCES):
        for b, bname in SOURCES[i+1:]:
            inter = len(sets[a] & sets[b])
            union = len(sets[a] | sets[b])
            j = inter / union if union else 0.0
            containment_a = inter / len(sets[a]) if sets[a] else 0.0
            containment_b = inter / len(sets[b]) if sets[b] else 0.0
            pair_rows.append({
                "source_a": aname,
                "source_b": bname,
                "a_types": len(sets[a]),
                "b_types": len(sets[b]),
                "exact_shared_forms": inter,
                "exact_union_forms": union,
                "jaccard": f"{j:.8f}",
                "share_of_a_found_in_b": f"{containment_a:.8f}",
                "share_of_b_found_in_a": f"{containment_b:.8f}",
            })
    pair_path = OUT / "Data" / "PAIRWISE_EXACT_SURFACE_COMPARISON.tsv"
    with pair_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(pair_rows[0]), delimiter="\t")
        writer.writeheader(); writer.writerows(pair_rows)

    # Per-source summary data.
    source_rows = []
    unique_by_source = {}
    shared_by_source = {}
    for folder, name in SOURCES:
        unique = sum(1 for form in sets[folder] if len(membership[form]) == 1)
        shared = len(sets[folder]) - unique
        unique_by_source[folder] = unique
        shared_by_source[folder] = shared
        m = manifests[folder]
        c = m["counts"]
        source_rows.append({
            "source": name,
            "folder": folder,
            "surface_types": len(sets[folder]),
            "wordlike_occurrences": c["wordlike_occurrences"],
            "raw_token_types": c["raw_token_types"],
            "source_unique_exact_forms": unique,
            "forms_shared_with_at_least_one_other_source": shared,
            "shared_percentage": pct(shared, len(sets[folder])),
            "nonspace_character_coverage": f"{c['covered_non_whitespace_characters']}/{c['non_whitespace_characters']}",
        })
    src_path = OUT / "Data" / "SOURCE_COMPARATIVE_SUMMARY.tsv"
    with src_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(source_rows[0]), delimiter="\t")
        writer.writeheader(); writer.writerows(source_rows)

    # Build the human-readable combined study.
    lines = []
    lines += [
        "# Kurdish-TSL — Combined Named-Source Research, Comparison, Results and Deep Conclusion V1",
        "",
        "## Method and evidential boundary",
        "",
        "This convergence layer combines the **already separate named-source evidence packages without erasing source identity**. Exact written forms that recur in more than one source are linked for comparison, but they are **not automatically treated as the same lemma, meaning, pronunciation, grammatical category, or historical form**.",
        "",
        "The active evidence used for quantitative comparison is the mechanically complete Deep Dictionary V1 layer. Earlier LDR material is retained as preliminary analysis. Agent-generated Stage-4 DSR/Unit1 grammatical studies remain preserved but are **not used as validated proof**, because the independent Stage-4 audit rejected their self-certification.",
        "",
        "The report is organized exactly as: **named source → research/evidence under that source → cross-source comparison → combined result → deep conclusion**.",
        "",
        "---",
        "",
    ]

    for idx, (folder, name) in enumerate(SOURCES, start=1):
        m = manifests[folder]
        c = m["counts"]
        s = sets[folder]
        unique = unique_by_source[folder]
        shared = shared_by_source[folder]
        top_freq = freqs[folder].most_common(20)
        top_cross = sorted(
            ((form, freqs[folder][form], len(membership[form])) for form in s if len(membership[form]) >= 2),
            key=lambda x: (-x[1], -x[2], x[0].casefold(), x[0]),
        )[:20]

        lines += [
            f"# {name} — Corpus {idx:03d}",
            "",
            f"**Repository identity:** `{folder}`  ",
            f"**Dictionary status:** `{m['dictionary_status']}`  ",
            f"**Exact word-like surface forms:** **{len(s):,}**  ",
            f"**Word-like occurrences:** **{c['wordlike_occurrences']:,}**  ",
            f"**Raw token types:** **{c['raw_token_types']:,}**  ",
            f"**Non-whitespace character coverage:** **{c['covered_non_whitespace_characters']:,}/{c['non_whitespace_characters']:,}**  ",
            "",
            "## Research/evidence under this source",
            "",
            f"- Exact forms occurring only in {name} within the current 14-source collection: **{unique:,}** ({pct(unique, len(s))}).",
            f"- Exact forms also attested in at least one other named source: **{shared:,}** ({pct(shared, len(s))}).",
            "- These are exact-surface comparisons only. A shared spelling is a convergence candidate, not an established shared lemma or meaning.",
            "",
            "### Existing research artifacts and their status",
            "",
        ]
        for path, status in list_research_artifacts(folder):
            lines.append(f"- `{path}` — **{status}**")
        lines += ["", "### Highest-frequency exact forms in this source", "", "| Exact form | Frequency |", "|---|---:|"]
        for form, n in top_freq:
            lines.append(f"| `{md_escape(form)}` | {n:,} |")
        lines += ["", "### High-frequency forms also attested in other named sources", "", "| Exact form | Frequency here | Number of named sources containing the exact form |", "|---|---:|---:|"]
        if top_cross:
            for form, n, sc in top_cross:
                lines.append(f"| `{md_escape(form)}` | {n:,} | {sc} |")
        else:
            lines.append("| — | — | — |")
        lines += ["", "---", ""]

    # Global comparison.
    lines += [
        "# Cross-source comparison",
        "",
        "## Corpus scale and exact-surface sharing",
        "",
        "| Named source | Exact surface forms | Word-like occurrences | Source-unique exact forms | Shared with ≥1 other source | Shared % |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in source_rows:
        lines.append(
            f"| {row['source']} | {row['surface_types']:,} | {row['wordlike_occurrences']:,} | {row['source_unique_exact_forms']:,} | {row['forms_shared_with_at_least_one_other_source']:,} | {row['shared_percentage']} |"
        )

    lines += [
        "",
        "## Global exact-surface recurrence",
        "",
        f"- Union of distinct exact written surface forms across all named sources: **{global_union:,}**.",
        f"- Exact forms attested in at least two named sources: **{shared_2plus:,}** ({pct(shared_2plus, global_union)} of the union).",
        f"- Exact forms attested in all 14 named sources: **{shared_all:,}**.",
        "",
        "| Number of named sources containing an exact form | Number of exact forms |",
        "|---:|---:|",
    ]
    for k in sorted(incidence):
        lines.append(f"| {k} | {incidence[k]:,} |")

    lines += [
        "",
        "## Strongest pairwise exact-surface overlaps",
        "",
        "Jaccard = exact shared forms / exact union forms. This is an orthographic evidence statistic, not a grammatical or semantic similarity score.",
        "",
        "| Source A | Source B | Shared exact forms | Jaccard | % of A found in B | % of B found in A |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for row in sorted(pair_rows, key=lambda r: (-float(r["jaccard"]), -r["exact_shared_forms"]))[:30]:
        lines.append(
            f"| {row['source_a']} | {row['source_b']} | {row['exact_shared_forms']:,} | {float(row['jaccard']):.4f} | {100*float(row['share_of_a_found_in_b']):.2f}% | {100*float(row['share_of_b_found_in_a']):.2f}% |"
        )

    # Most widely recurring exact forms.
    widely = sorted(membership, key=lambda f: (-len(membership[f]), -global_frequency[f], f.casefold(), f))[:100]
    lines += [
        "",
        "## Most widely recurring exact written forms",
        "",
        "These forms are prioritized for later independent lexical interpretation because recurrence across independently preserved sources provides stronger documentary leverage. Recurrence alone does not establish meaning.",
        "",
        "| Exact form | Named-source count | Total corpus occurrence frequency | Sources |",
        "|---|---:|---:|---|",
    ]
    for form in widely:
        srcs = ", ".join(DISPLAY[x] for x in membership[form])
        lines.append(f"| `{md_escape(form)}` | {len(membership[form])} | {global_frequency[form]:,} | {md_escape(srcs)} |")

    lines += [
        "",
        "# Final combined result",
        "",
        "1. **The fourteen corpora can now be studied as one comparative documentary system without destroying their independence.** Each exact form retains its named-source membership, and every cross-source recurrence can be traced back to the source-specific dictionary packages.",
        "2. **The combined layer is substantially smaller than the simple sum of corpus-local entries whenever exact spellings recur across sources.** This allows the project to distinguish source-specific written forms from cross-source recurrent forms while still preserving every original entry.",
        "3. **Cross-source recurrence creates a principled priority system for deeper interpretation.** Forms occurring in many independent sources are high-value candidates for later semantic, structural, and historical investigation; forms confined to one source remain equally preserved but require stronger caution because uniqueness may reflect genre, date, names, spelling, editorial practice, OCR, or limited sampling.",
        "4. **Corpus sizes are extremely unequal.** ANHA, Ronahî, and especially Rudaw contain far more written material than several historical/pedagogical corpora. Raw counts therefore cannot be interpreted as linguistic importance. Comparison must use source incidence, normalized proportions, and source-aware evidence rather than frequency alone.",
        "5. **The previous failed Stage-4 self-certification is not rehabilitated by lexical convergence.** Exact spelling overlap is genuine mechanical evidence, but it cannot by itself validate claims about grammatical category, word order, morphology, tense/aspect, case, ergativity, or meaning.",
        "",
        "# Deep conclusion",
        "",
        "The project has now moved from **isolated archives** to a **provenance-preserving convergence architecture**. The correct unit of comparison is not an assumed Kurdish lemma but an attested written form linked to its named sources, frequencies, locations, and contexts. This changes the research logic: instead of starting from a pre-existing dictionary or grammar and asking where it appears, we can start from independently attested evidence and ask which relationships survive across sources.",
        "",
        "The deepest result at this stage is therefore methodological and empirical rather than grammatical. There is now a recoverable path from **Mem û Zîn / ANHA / Ronahî / Rudaw / Pirtûkên Kurmancî Katalog / Kurmanji Beginners / Kovara Kurmancî / Kovara Hawar / Rojnama Kurdistan / Kovara Jîn / Folklora Kurmanca / Kurd Teavun Terakki / Rojî Kurd / Dîrok û Civaka Kurdan** to every combined exact-form comparison. This permits future hypotheses to be ranked by independent-source support instead of by familiarity or model expectation.",
        "",
        "The next scientifically valid interpretive step is to take the strongest recurrent-form candidates and reconstruct their contextual behavior separately inside each named source before proposing any shared lexical meaning or grammatical function. Agreement across independently analyzed sources can then raise confidence; disagreement becomes a research target rather than something to normalize away.",
        "",
        "## Machine-readable comparative outputs",
        "",
        "- `Data/EXACT_SURFACE_CROSS_SOURCE_INDEX.tsv.gz` — exhaustive exact-form union with named-source memberships and aggregate frequencies.",
        "- `Data/SOURCE_COMPARATIVE_SUMMARY.tsv` — one-row-per-source comparative metrics.",
        "- `Data/PAIRWISE_EXACT_SURFACE_COMPARISON.tsv` — all pairwise exact-surface intersection, union, Jaccard and containment measures.",
    ]

    report = OUT / "TSLK_COMBINED_NAMED_SOURCE_RESEARCH_V1.md"
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")

    build_manifest = {
        "version": "TSLK_COMPARATIVE_RESEARCH_V1",
        "source_count": len(SOURCES),
        "source_names": [name for _, name in SOURCES],
        "global_exact_surface_union": global_union,
        "exact_forms_shared_by_2plus_sources": shared_2plus,
        "exact_forms_shared_by_all_sources": shared_all,
        "corpus_local_surface_entries_sum": sum(len(sets[f]) for f, _ in SOURCES),
        "wordlike_occurrences_sum": sum(manifests[f]["counts"]["wordlike_occurrences"] for f, _ in SOURCES),
        "semantic_assignment_performed": False,
        "lemma_merging_performed": False,
        "grammatical_synthesis_performed": False,
        "stage4_failed_claims_used_as_proof": False,
        "outputs": [
            str(report.relative_to(ROOT)),
            str(index_path.relative_to(ROOT)),
            str(src_path.relative_to(ROOT)),
            str(pair_path.relative_to(ROOT)),
        ],
    }
    (OUT / "COMPARATIVE_BUILD_MANIFEST.json").write_text(json.dumps(build_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(build_manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
