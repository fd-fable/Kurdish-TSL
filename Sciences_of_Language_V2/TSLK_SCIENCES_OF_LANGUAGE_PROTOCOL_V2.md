# TSLK Sciences of Language Protocol V2

## Status

**FULL-OCCURRENCE STRUCTURAL RECONSTRUCTION PROTOCOL / DOCUMENTARY STREAM A ONLY**

## 1. Evidence hierarchy

1. primary source files;
2. CSTLK corpus evidence;
3. Deep Dictionary V1 occurrence rows;
4. audited Comparative Research V1;
5. Sciences of Language V1 structural candidates;
6. V2 full-occurrence measurements;
7. later interpretation only after derivational review.

Previously learned Kurdish-specific knowledge is inadmissible as evidence. Every language-specific conclusion must have a recoverable evidential path to the committed corpus evidence.

## 2. Full-coverage requirement

Every committed `Dictionaries/<CORPUS>/Occurrences/OCCURRENCES_*.tsv.gz` row must be read exactly once by its source-local V2 scan for coverage accounting. The scan must reconcile its observed occurrence total with the corresponding Deep Dictionary manifest.

A failed reconciliation invalidates that corpus V2 package.

## 3. Documentary stream and structural-candidate stream

### D — Documentary stream

All occurrence rows are counted for provenance and coverage, including digits, metadata, URLs, headings, foreign-language strings, names, extraction artifacts, and unresolved material.

### C — Structural-candidate stream

A token may enter C when it:

- contains at least one Unicode letter;
- contains no Unicode numeric character;
- is not a Comparative Research V1 repeated-context/template-risk form;
- does not occur in a container mechanically flagged by explicit URL/technical-context markers.

This is **not a Kurdish-language-membership classifier**. Material in C remains `LANGUAGE MEMBERSHIP UNRESOLVED`.

## 4. Container integrity

No n-gram or construction may cross a `container_locator` boundary. Token order is taken from `token_index` within the original container. Any discontinuity or ordering anomaly must be counted in the corpus audit.

## 5. Continuous sequence discovery

For every eligible contiguous C-run inside a container, measure:

- bigrams;
- trigrams;
- four-token sequences.

Per-corpus packages may retain only recurrent patterns (`support >= 2`) because a sequence seen once cannot support a recurrence hypothesis. The scan itself remains exhaustive.

Cross-source promotion requires at least two independent named sources unless explicitly marked `SOURCE-LOCAL ONLY`.

## 6. Variable-slot frames

For each eligible trigram `A X B`, derive the neutral frame:

`A + SLOT + B`

Record:

- total support;
- distinct filler count;
- filler entropy where practical;
- top fillers;
- source incidence.

A frame is not automatically a syntactic construction. It is a `VARIABLE-SLOT FRAME CANDIDATE`.

## 7. Discontinuous relations

Measure endpoint relations with exact intervening gap sizes 1–3:

- `A _ B` (one intervening token);
- `A _ _ B`;
- `A _ _ _ B`.

Record gap size, support, source incidence, and source distribution. These are `DISCONTINUOUS RELATION CANDIDATES`, not dependencies.

## 8. Position system

For eligible occurrences, calculate within-container normalized position deciles and exact initial/final counts. Positional profiles are descriptive and cannot define a class that is then tested for that same position.

## 9. Morphology V2

V1 edge-extension candidates are re-tested against complete occurrence contexts.

For a form-family candidate `F ↔ F+x` or `x+F ↔ F`, V2 may measure:

- full occurrence support of both forms;
- complete immediate-context distributions;
- context overlap/similarity;
- source-local support;
- source incidence;
- contexts favoring one form over the other;
- counterexamples/low-overlap cases.

The added material remains `EDGE MATERIAL / FUNCTION UNRESOLVED` until independent interpretation is justified.

## 10. Evidence scores

Scores rank evidence only.

### Cross-Source Construction Evidence Score (CCES)

A reproducible 0–100 ranking based on:

- source diversity;
- normalized support;
- source-distribution entropy;
- recurrence complexity (sequence length or filler diversity);
- documentary-risk penalty.

### Morphology Context Evidence Score V2 (MCES2)

A reproducible 0–100 ranking based on:

- source diversity;
- minimum support for both related forms;
- complete-context similarity;
- form-pair recurrence;
- documentary-risk penalty.

No score is a correctness probability.

## 11. Cross-source aggregation

Every corpus is first processed independently. Aggregation may link identical exact patterns across corpora, but identical strings are not automatically assigned identical meanings, lemmas, pronunciations, or grammatical functions.

## 12. Source imbalance

Raw total support must never be the only ranking criterion. Source incidence, normalized support, and source-distribution entropy are required because ANHA/Rudaw are much larger than historical corpus slices.

## 13. Literature/register variation

V2 may compare structural distributions across named sources, but conclusions apply only to the text actually committed. Sources 007–014 remain sparse witnesses until their CSTLK coverage is expanded.

## 14. Language Graph V2

Permitted node types include:

- `SOURCE`
- `FORM`
- `CONTINUOUS_SEQUENCE`
- `VARIABLE_SLOT_FRAME`
- `DISCONTINUOUS_PATTERN`
- `EDGE_MATERIAL_PATTERN`
- `FORM_FAMILY_CANDIDATE`

Permitted edge types include:

- `SOURCE_ATTESTS_FORM`
- `SOURCE_ATTESTS_PATTERN`
- `SEQUENCE_CONTAINS_FORM`
- `FRAME_HAS_FIXED_LEFT`
- `FRAME_HAS_FIXED_RIGHT`
- `FORM_FILLS_FRAME_SLOT`
- `FORM_FAMILY_RELATION`
- `PATTERN_SUPPORTS_HYPOTHESIS` (only in later interpretive layers)
- `EVIDENCE_CONTRADICTS_HYPOTHESIS` (only in later interpretive layers)

Graph topology is evidence representation, not linguistic ontology.

## 15. Required audits

Each corpus package must expose:

- expected occurrence rows;
- scanned occurrence rows;
- container count;
- ordering anomalies;
- documentary-risk occurrence count;
- candidate-stream occurrence count;
- retained bigram/trigram/fourgram counts;
- retained variable-slot and discontinuous candidate counts;
- explicit thresholds.

The aggregate package must fail if any corpus manifest fails coverage.

## 16. Research-stream isolation

Native-speaker/user evidence is not used in V2. Stream B remains isolated until an explicit later convergence phase.

## 17. Promotion rule

A conventional grammatical or morphological label may only be introduced in a later interpretive study when:

1. the underlying pattern is recoverable from V2 evidence;
2. competing analyses are stated;
3. counterexamples are inspected;
4. the label explains more evidence than its competitors;
5. prior Kurdish knowledge is not used as the evidential premise.
