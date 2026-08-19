# Corpus Use Policy — Discovery Phase

## Purpose
The repository contains different kinds of material. They must not all be treated as equivalent evidence for discovering grammar.

A corpus can be useful while still being unsuitable as the **first** source of grammatical hypotheses. The manager must assign each corpus a role before analysis.

## Evidence roles

### PRIMARY-DISCOVERY
Naturalistic running text suitable for generating first-pass observations after text quality has been checked.

### CROSS-TEST
Independent text used mainly to test whether a pattern discovered elsewhere survives changes in author, genre, date, or editorial tradition.

### HISTORICAL/GENRE-SPECIFIC
Valuable linguistic evidence, but its patterns must initially be treated as local to its period, genre, or editorial tradition.

### HOLDOUT-METALINGUISTIC
Material that may explicitly teach or discuss the language. Do not use it to generate the blind grammar. Reserve it for later comparison or carefully isolate non-metalinguistic passages.

### METADATA/LEXICAL
Catalogs, lists, bibliographic material, indexes, or other material that may support orthographic/lexical observations but should not be treated as ordinary continuous discourse.

### LEGACY-ANALYSIS
Existing analysis, diagnosis, or grammar documents. Excluded from discovery evidence.

## Preliminary corpus roles
These are operational safeguards, not linguistic judgments. The role may be refined after source inspection.

| Corpus | Preliminary role | Discovery-phase use |
|---|---|---|
| `001_MEM_U_ZIN` | HISTORICAL/GENRE-SPECIFIC | Classical/literary evidence; strong for cross-testing, but do not assume poetic distributions generalize to modern prose. |
| `002_ANHA` | PRIMARY-DISCOVERY | Naturalistic modern journalistic prose; suitable for generating observations after source/recovery audit. |
| `003_RONAHI` | PRIMARY-DISCOVERY | Independent modern journalistic corpus; use for discovery and cross-testing against ANHA. |
| `004_RUDAW` | PRIMARY-DISCOVERY | Large independent modern journalistic corpus; useful for distributional tests and counterexample search. |
| `005_PIRTUKEN_KURMANCI_KATALOG` | METADATA/LEXICAL | Use for names, titles, orthographic/lexical evidence where appropriate; do not infer ordinary sentence grammar from catalog structure. |
| `006_KURMANJI_BEGINNERS` | HOLDOUT-METALINGUISTIC | Beginner instructional material can encode an external grammatical analysis. Keep out of blind discovery; use later for comparison/validation. |
| `007_KOVARA_KURMANCI` | HOLDOUT-METALINGUISTIC / MIXED | Inspect article-level content first. Language-focused articles may explicitly discuss grammar; only clearly non-metalinguistic running text may enter blind discovery. |
| `008_KOVARA_HAWAR` | HISTORICAL/GENRE-SPECIFIC | Historical corpus; recover carefully and use to test diachronic/editorial stability. |
| `009_ROJNAMA_KURDISTAN` | HISTORICAL/GENRE-SPECIFIC | Historical newspaper evidence; cross-test rather than automatically merging with modern distributions. |
| `010_KOVARA_JIN` | HISTORICAL/GENRE-SPECIFIC | Historical magazine evidence; preserve source-specific orthography and variation. |
| `011_FOLKLORA_KURMANCA_1936` | HISTORICAL/GENRE-SPECIFIC | Folkloric material may show genre/register effects; use as an independent test domain. |
| `012_KURD_TEAVUN_TERAKKI_1908` | HISTORICAL/GENRE-SPECIFIC | Early-period material; strong diachronic evidence after script/OCR/source checks. |
| `013_ROJI_KURD_1913` | HISTORICAL/GENRE-SPECIFIC | Historical journal material; test independently before pooling. |
| `014_DIROK_U_CIVAKA_KURDAN` | CROSS-TEST / HISTORICAL-GENRE REVIEW | Inspect composition and provenance first; use as an independent prose domain when text type is established. |

## Legacy material
The following role is fixed during discovery:

- `LDRSTLK000MASTERGRAMMAR08172026FDA.docx` — LEGACY-ANALYSIS
- all numbered `LDRSTLK*` documents — LEGACY-ANALYSIS
- all files under `Linguistic_Diagnosis_Reports/` — LEGACY-ANALYSIS

They must not be inputs to blind discovery.

## Recommended discovery sequence
1. Select a bounded, auditable slice of `002_ANHA`.
2. Verify/recover the text without grammatical normalization.
3. Produce observations with neutral labels only.
4. Test the same candidate patterns against `003_RONAHI`.
5. Search the much larger `004_RUDAW` corpus for support and counterexamples.
6. Only then test historical/literary corpora one by one, keeping date/genre effects visible.
7. Keep `006_KURMANJI_BEGINNERS`, metalinguistic parts of `007_KOVARA_KURMANCI`, and all legacy analysis sealed until the corpus-derived system is sufficiently mature for comparison.

## Pooling rule
Never merge evidence from all corpora into one undifferentiated count. Every observation must retain corpus identity. A pattern may be:
- source-local;
- genre-local;
- period-local;
- widespread;
- unresolved.

The project should discover those differences rather than normalize them away.
