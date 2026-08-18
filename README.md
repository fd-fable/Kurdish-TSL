# Kurdish-TSL — The Sciences of Language

Kurdish-TSL is a corpus-centered project for recovering, comparing, and studying Kurdish (Kurmancî) texts across different periods, genres, and sources.

## Current research phase: discover before formalizing

The project is currently in a **grammar-discovery phase**.

The immediate objective is **not** to take an existing Kurmancî grammar and apply it to these texts. The objective is to:

1. preserve the original sources;
2. recover the clearest faithful text possible;
3. observe recurrent forms and distributions without imposing inherited grammatical categories;
4. form hypotheses from corpus evidence;
5. test those hypotheses across independent corpora;
6. synthesize a grammar only after patterns survive repeated testing;
7. compare with external grammars and implement computational rules later.

See `AGENTS.md` for the project-wide evidence rules and phase boundaries.

## Evidence discipline

Every analytical claim must be distinguishable as:

- **OBSERVED** — directly present in cited corpus evidence;
- **INFERRED** — a hypothesis induced from observations;
- **EXTERNAL** — knowledge from outside the corpus.

During the current discovery phase, EXTERNAL knowledge is not admissible as evidence for deciding the grammar.

Agents should use neutral descriptive labels such as `FORM-001`, `PATTERN-A`, or `SLOT-2` until the corpus itself supports a more functional description.

## Repository structure

### Numbered corpora

- `001_MEM_U_ZIN` — Mem û Zîn classical-text corpus and source materials.
- `002_ANHA` — ANHA journalistic corpus and source materials.
- `003_RONAHI` — Ronahî corpus and source materials.
- `004_RUDAW` — Rûdaw corpus and source materials.
- `005_PIRTUKEN_KURMANCI_KATALOG` — Kurdish book-catalog material.
- `006_KURMANJI_BEGINNERS` — introductory/learning-text corpus.
- `007_KOVARA_KURMANCI` — Kovara Kurmancî material.
- `008_KOVARA_HAWAR` — Hawar historical collection.
- `009_ROJNAMA_KURDISTAN` — Kurdistan newspaper historical corpus.
- `010_KOVARA_JIN` — Jin magazine historical corpus.
- `011_FOLKLORA_KURMANCA_1936` — Folklora Kurmanca corpus.
- `012_KURD_TEAVUN_TERAKKI_1908` — Kurd Teavun ve Terakki material.
- `013_ROJI_KURD_1913` — Roji Kurd historical journal corpus.
- `014_DIROK_U_CIVAKA_KURDAN` — history-and-society collection.

Numbered corpus directories generally preserve compiled corpus documents together with their source materials. Source provenance should remain traceable.

### Aggregated corpus material

- `Kurdish_Corpora_Word_Docs/` — compiled corpus documents and article audit records.
- `Sources/` and `books_sources/` — source documents, digitized material, and extraction/OCR support data.

### Legacy/preliminary analysis

The repository also preserves an earlier analytical layer:

- `LDRSTLK000MASTERGRAMMAR08172026FDA.docx`
- numbered-corpus documents beginning with `LDRSTLK`
- `Linguistic_Diagnosis_Reports/`

These files are **not discovery evidence**. They may contain prior grammatical assumptions. Preserve them for historical record and later blind comparison, but do not feed them to discovery agents while the corpus-derived grammar is being built. See `LEGACY_ANALYSIS_NOTICE.md`.

## Agent prompts

- `prompts/TEXT_RECOVERY_AGENT.md` — recover faithful text without grammar-based correction.
- `prompts/GRAMMAR_DISCOVERY_AGENT.md` — observe, induce, falsify, and cross-test patterns using neutral labels.
- `prompts/MANAGER_AGENT.md` — coordinate the process, enforce evidence classes, and prevent prior-grammar leakage.

## Discovery workflow

### Phase 0 — preserve sources and provenance
Keep original material unchanged and record what each recovered text came from.

### Phase 1 — recover clear text
Repair demonstrable OCR, encoding, or layout corruption only. Preserve uncertain, historical, dialectal, and source-specific forms rather than silently normalizing them.

### Phase 2 — observe
Record recurrence, alternation, ordering, adjacency, distribution, and boundary behavior. Do not explain a pattern before documenting it.

### Phase 3 — hypothesize
Propose minimal, falsifiable explanations from accumulated observations. Keep competing explanations when the evidence is insufficient.

### Phase 4 — cross-test
Test candidates against independent texts from different genres, dates, authors, and sources. Search actively for counterexamples.

### Phase 5 — synthesize grammar
Introduce stable descriptive rules only after repeated corpus support, with an evidence trail attached to each rule.

### Phase 6 — compare and implement
Only after independent discovery should the project compare its system with published grammars, legacy diagnosis documents, dictionaries, parsers, or other external descriptions. Grammar-engine or parser implementation belongs after this stage begins.

## Current principle

**Clear text first. Observation second. Grammar discovery third. Formalization and programming later.**
