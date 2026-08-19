#!/usr/bin/env python3
"""Audit/refine the combined named-source comparison.

Keeps the exhaustive documentary comparison intact, then creates a second
letter-bearing lexical-candidate layer and a repeated-first-context reuse flag
so document templates/front matter are not mistaken for language convergence.
No language membership, meaning, lemma, or grammatical function is assigned.
"""
from __future__ import annotations

import csv
import gzip
import json
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DROOT = ROOT / "Dictionaries"
OUT = ROOT / "Comparative_Research_V1"
DATA = OUT / "Data"

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


def is_letter_candidate(form: str) -> bool:
    cats = [unicodedata.category(ch) for ch in form]
    has_letter = any(c.startswith("L") for c in cats)
    has_number = any(c.startswith("N") for c in cats)
    return has_letter and not has_number


def load_source(folder: str):
    entries = {}
    files = sorted((DROOT / folder).glob("LEXICON_*.tsv"))
    if not files and (DROOT / folder / "LEXICON.tsv").exists():
        files = [DROOT / folder / "LEXICON.tsv"]
    for p in files:
        with p.open("r", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                form = row.get("surface_form", "")
                if not form or not is_letter_candidate(form):
                    continue
                try:
                    freq = int(row.get("frequency", "0") or 0)
                except ValueError:
                    freq = 0
                entries[form] = {
                    "frequency": freq,
                    "first_context": row.get("first_context", "") or "",
                }
    return entries


def pct(n, d):
    return "0.00%" if not d else f"{100*n/d:.2f}%"


def esc(s):
    return s.replace("|", "\\|").replace("\n", " ")


def main():
    entries = {f: load_source(f) for f, _ in SOURCES}
    sets = {f: set(entries[f]) for f, _ in SOURCES}
    membership = defaultdict(list)
    global_freq = Counter()
    contexts = defaultdict(Counter)

    for folder, _ in SOURCES:
        for form, meta in entries[folder].items():
            membership[form].append(folder)
            global_freq[form] += meta["frequency"]
            context = meta["first_context"].strip()
            if context:
                contexts[form][context] += 1

    def max_same_context(form):
        return max(contexts[form].values(), default=0)

    def template_risk(form):
        return len(membership[form]) >= 3 and max_same_context(form) >= 3

    union = len(membership)
    shared2 = sum(1 for f in membership if len(membership[f]) >= 2)
    shared14 = sum(1 for f in membership if len(membership[f]) == 14)
    template_risk_count = sum(1 for f in membership if template_risk(f))
    cross_candidate = sum(1 for f in membership if len(membership[f]) >= 2 and not template_risk(f))

    # Exhaustive letter-bearing cross-source index.
    idx_path = DATA / "LETTER_BEARING_CROSS_SOURCE_INDEX.tsv.gz"
    with gzip.open(idx_path, "wt", encoding="utf-8", newline="") as gz:
        fields = [
            "surface_form", "source_count", "sources", "global_occurrence_frequency",
            "max_identical_first_context_sources", "repeated_context_template_risk",
            "language_membership_status"
        ]
        w = csv.DictWriter(gz, fieldnames=fields, delimiter="\t")
        w.writeheader()
        for form in sorted(membership, key=lambda x: (x.casefold(), x)):
            w.writerow({
                "surface_form": form,
                "source_count": len(membership[form]),
                "sources": " | ".join(f"{DISPLAY[x]} [{x[:3]}]" for x in membership[form]),
                "global_occurrence_frequency": global_freq[form],
                "max_identical_first_context_sources": max_same_context(form),
                "repeated_context_template_risk": "YES" if template_risk(form) else "NO",
                "language_membership_status": "UNRESOLVED",
            })

    # Source summary for the letter-bearing layer.
    src_rows = []
    for folder, name in SOURCES:
        s = sets[folder]
        unique = sum(1 for form in s if len(membership[form]) == 1)
        shared = len(s) - unique
        risk = sum(1 for form in s if template_risk(form))
        shared_nonrisk = sum(1 for form in s if len(membership[form]) >= 2 and not template_risk(form))
        src_rows.append({
            "source": name,
            "folder": folder,
            "letter_bearing_exact_forms": len(s),
            "source_unique_letter_bearing_forms": unique,
            "shared_letter_bearing_forms": shared,
            "shared_non_template_risk_candidates": shared_nonrisk,
            "repeated_context_template_risk_forms": risk,
            "shared_percentage": pct(shared, len(s)),
        })
    src_path = DATA / "SOURCE_LETTER_BEARING_SUMMARY.tsv"
    with src_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(src_rows[0]), delimiter="\t")
        w.writeheader(); w.writerows(src_rows)

    # Pairwise letter-bearing exact-form comparison.
    pairs = []
    for i, (a, an) in enumerate(SOURCES):
        for b, bn in SOURCES[i+1:]:
            inter = len(sets[a] & sets[b])
            u = len(sets[a] | sets[b])
            pairs.append({
                "source_a": an, "source_b": bn,
                "a_letter_forms": len(sets[a]), "b_letter_forms": len(sets[b]),
                "shared_letter_forms": inter, "union_letter_forms": u,
                "jaccard": f"{(inter/u if u else 0):.8f}",
                "share_of_a_found_in_b": f"{(inter/len(sets[a]) if sets[a] else 0):.8f}",
                "share_of_b_found_in_a": f"{(inter/len(sets[b]) if sets[b] else 0):.8f}",
            })
    pair_path = DATA / "PAIRWISE_LETTER_BEARING_COMPARISON.tsv"
    with pair_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(pairs[0]), delimiter="\t")
        w.writeheader(); w.writerows(pairs)

    # Keep named source sections from the first build, replace the comparison/final layer.
    base_path = OUT / "TSLK_COMBINED_NAMED_SOURCE_RESEARCH_V1.md"
    base = base_path.read_text(encoding="utf-8")
    prefix = base.split("# Cross-source comparison", 1)[0].rstrip()
    scope_note = """

> **Comparative lexical-scope audit:** The exhaustive mechanical dictionaries intentionally preserve digits, headings, front matter, bibliography/citation material, other-language strings, and possible technical/template text. Therefore the source sections above are documentary inventories. The audited comparison below introduces a separate **letter-bearing / no-numeric lexical-candidate layer** and a **repeated-first-context template-risk flag**. Even this filtered layer does not automatically establish that a form belongs to Kurdish; language membership remains `UNRESOLVED` until source-internal evidence supports it.
""".rstrip()

    out = [prefix, scope_note, "", "# Cross-source comparison — audited convergence layer", ""]
    out += [
        "## 1. Documentary baseline (all mechanically preserved forms)", "",
        "The exhaustive all-form comparison remains preserved in `Data/EXACT_SURFACE_CROSS_SOURCE_INDEX.tsv.gz`. It is a documentary coverage layer, not a language-purity filter.", "",
        "## 2. Letter-bearing lexical-candidate comparison", "",
        f"- Distinct letter-bearing, no-numeric exact surface forms across the fourteen named sources: **{union:,}**.",
        f"- Letter-bearing exact forms attested in at least two named sources: **{shared2:,}** ({pct(shared2, union)}).",
        f"- Letter-bearing exact forms attested in all fourteen named sources: **{shared14:,}**.",
        f"- Forms mechanically flagged for repeated identical first-context reuse across ≥3 sources: **{template_risk_count:,}**.",
        f"- Cross-source letter-bearing candidates shared by ≥2 sources after excluding that repeated-context risk flag: **{cross_candidate:,}**.",
        "- The template-risk flag is conservative and mechanical; `NO` does not prove a form is Kurdish, and `YES` does not prove the form is non-Kurdish.",
        "",
        "| Named source | Letter-bearing exact forms | Source-unique | Shared ≥2 | Shared non-template-risk candidates | Repeated-context risk | Shared % |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for r in src_rows:
        out.append(f"| {r['source']} | {r['letter_bearing_exact_forms']:,} | {r['source_unique_letter_bearing_forms']:,} | {r['shared_letter_bearing_forms']:,} | {r['shared_non_template_risk_candidates']:,} | {r['repeated_context_template_risk_forms']:,} | {r['shared_percentage']} |")

    out += ["", "## 3. Strongest pairwise letter-bearing exact-surface overlaps", "",
            "| Source A | Source B | Shared letter-bearing exact forms | Jaccard | % of A found in B | % of B found in A |",
            "|---|---|---:|---:|---:|---:|"]
    for r in sorted(pairs, key=lambda x: (-float(x['jaccard']), -x['shared_letter_forms']))[:30]:
        out.append(f"| {r['source_a']} | {r['source_b']} | {r['shared_letter_forms']:,} | {float(r['jaccard']):.4f} | {100*float(r['share_of_a_found_in_b']):.2f}% | {100*float(r['share_of_b_found_in_a']):.2f}% |")

    ranked = sorted(
        (form for form in membership if len(membership[form]) >= 2 and not template_risk(form)),
        key=lambda form: (-len(membership[form]), -global_freq[form], form.casefold(), form),
    )[:100]
    out += ["", "## 4. Widely recurrent letter-bearing candidates after repeated-context risk exclusion", "",
            "Every item below remains **LANGUAGE MEMBERSHIP UNRESOLVED**. It is prioritized because the same exact written form recurs across independently preserved sources without triggering the repeated-first-context reuse flag.", "",
            "| Exact form | Named-source count | Aggregate occurrence frequency | Language membership | Sources |",
            "|---|---:|---:|---|---|"]
    for form in ranked:
        out.append(f"| `{esc(form)}` | {len(membership[form])} | {global_freq[form]:,} | UNRESOLVED | {esc(', '.join(DISPLAY[x] for x in membership[form]))} |")

    out += [
        "", "# Final combined result", "",
        "1. **The named sources are now computationally connected without being collapsed.** Mem û Zîn, ANHA, Ronahî, Rudaw, Pirtûkên Kurmancî Katalog, Kurmanji Beginners, Kovara Kurmancî, Kovara Hawar, Rojnama Kurdistan, Kovara Jîn, Folklora Kurmanca, Kurd Teavun Terakki, Rojî Kurd, and Dîrok û Civaka Kurdan each retain their own evidence block and corpus-local dictionary.",
        "2. **The project now has two convergence layers rather than one misleading merged vocabulary.** The documentary layer preserves every exact mechanical form. The lexical-candidate layer removes numeric forms and explicitly marks repeated identical-context reuse risk, while still refusing to assign language identity automatically.",
        "3. **Cross-source recurrence is useful as evidence prioritization, not as proof of meaning or grammar.** A recurring exact form deserves investigation in each source, but it cannot be declared one lemma or one grammatical element until its source-internal contexts support that relation.",
        "4. **Standardized corpus/template material is empirically visible.** Repetition across many files can arise from shared document construction as well as from the language. This means source-count alone is insufficient; context independence is part of the convergence test.",
        "5. **Source imbalance remains substantial.** Large modern corpora contribute far more types and occurrences than small historical or pedagogical corpora. Source incidence and containment measures are therefore more informative for convergence than raw aggregate frequency alone.",
        "6. **The failed Stage-4 grammar certification remains excluded.** The combined lexical evidence does not validate prior claims about morphology, word order, tense/aspect, case, ergativity, or syntactic categories.",
        "", "# Deep conclusion", "",
        "The combined system now supports a stronger research question than 'What words are in all the files?': **Which exact written relationships survive independent source boundaries after documentary/template effects are exposed, and what do those recurring forms do inside each source?**",
        "",
        "This matters because a naive merged dictionary would erase the experiment. If fourteen files were collapsed into one bag of tokens, we could no longer tell whether a form is stable across historical periods, genres, editorial systems, or only frequent in one huge modern corpus. The new convergence architecture keeps both facts simultaneously: one searchable cross-source index and fourteen independent evidential histories.",
        "",
        "The most defensible next interpretive unit is therefore not a supposed lemma but a **cross-source candidate bundle**: exact form + named-source membership + frequency + source-specific contexts + template-risk status. Each candidate can then be analyzed independently in Mem û Zîn, ANHA, Ronahî, Rudaw, and the remaining sources. Only after those independent analyses agree should a shared lexical or structural hypothesis be proposed. Disagreement is retained as evidence of variation, ambiguity, genre, historical change, orthographic difference, or unresolved corpus composition rather than normalized away.",
        "",
        "In short, the project has moved from **separate corpora → exhaustive dictionaries → audited named-source convergence**. It has not yet moved to a unified Kurdish grammar or definitive dictionary of meanings, and doing so now would outrun the evidence.",
        "", "## Audited machine-readable outputs", "",
        "- `Data/EXACT_SURFACE_CROSS_SOURCE_INDEX.tsv.gz` — exhaustive documentary union (all mechanical forms).",
        "- `Data/LETTER_BEARING_CROSS_SOURCE_INDEX.tsv.gz` — letter-bearing/no-numeric candidate union with template-context risk and language-membership status.",
        "- `Data/SOURCE_COMPARATIVE_SUMMARY.tsv` — documentary source summary.",
        "- `Data/SOURCE_LETTER_BEARING_SUMMARY.tsv` — audited lexical-candidate source summary.",
        "- `Data/PAIRWISE_EXACT_SURFACE_COMPARISON.tsv` — all-form pairwise comparison.",
        "- `Data/PAIRWISE_LETTER_BEARING_COMPARISON.tsv` — letter-bearing pairwise comparison.",
    ]

    final_path = OUT / "TSLK_COMBINED_NAMED_SOURCE_RESEARCH_V1_FINAL.md"
    final_path.write_text("\n".join(out) + "\n", encoding="utf-8")

    audit_manifest = {
        "version": "TSLK_COMPARATIVE_RESEARCH_V1_FINAL",
        "named_sources": [name for _, name in SOURCES],
        "letter_bearing_no_numeric_union": union,
        "letter_bearing_shared_2plus": shared2,
        "letter_bearing_shared_all_14": shared14,
        "repeated_first_context_template_risk_forms": template_risk_count,
        "shared_2plus_after_template_risk_exclusion": cross_candidate,
        "language_membership_assignment_performed": False,
        "semantic_assignment_performed": False,
        "lemma_merging_performed": False,
        "grammar_synthesis_performed": False,
        "numeric_documentary_forms_deleted": False,
        "documentary_baseline_preserved": True,
        "final_report": str(final_path.relative_to(ROOT)),
    }
    (OUT / "COMPARATIVE_AUDIT_MANIFEST.json").write_text(json.dumps(audit_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(audit_manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
