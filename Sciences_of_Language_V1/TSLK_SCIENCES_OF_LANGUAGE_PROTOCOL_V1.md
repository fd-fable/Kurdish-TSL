# TSLK Sciences of Language Protocol V1

## Purpose

Build a research-grade structural model of the language from the committed corpus evidence without importing inherited Kurdish grammar as discovery evidence.

## Evidence hierarchy

1. Primary Sources
2. CSTLK corpus evidence
3. Deep Dictionary V1 exact-form and occurrence evidence
4. Comparative Research V1 audited cross-source convergence
5. Sciences of Language V1 derived structural evidence
6. Later interpretive terminology only after derivational review

## 1. Word structure

A written form is first treated as an exact graphemic sequence. Record length, edge strings, frequency, source distribution, position counts, neighbor profiles, and cross-source recurrence.

## 2. Morphological-candidate discovery

The system may mechanically identify relations such as one exact form being a left-edge or right-edge extension of another exact form. Such a relation is named an `EDGE-EXTENSION CANDIDATE`, not a prefix/suffix/morpheme.

A recurring added string may be promoted to an `EDGE-MATERIAL PATTERN` only when multiple independent form pairs support it. Semantic or grammatical function remains unresolved.

## 3. Structural / grammar-candidate discovery

Immediate-neighbor relations from the dictionary evidence may be aggregated across sources. A directed relation A→B is a `STRUCTURAL NEIGHBOR CANDIDATE`, not a syntactic dependency.

Position evidence may identify recurrent container-initial or container-final tendencies. These are positional tendencies, not assumed grammatical categories.

## 4. Evidence scores

Scores are documentary evidence-strength scores from 0–100, never correctness probabilities.

### Structural Evidence Score (SES)

For a candidate relation:

- 45% source diversity
- 35% normalized aggregate support
- 20% normalized source-distribution entropy

High SES means the relation is independently recurrent, sufficiently supported, and not dominated by only one source.

### Form-Family Evidence Score (FFES)

For an exact base↔extended relation:

- 40% source diversity
- 30% normalized aggregate support
- 30% observed neighbor-context similarity

High FFES means the written relation recurs independently and the two forms participate in partly similar local distributions. It does not prove morphological derivation.

## 5. Literature / register profile

Each named source retains its own descriptive domain and quantitative profile. Metrics include corpus scale, type/token relation, one-occurrence-form share, cross-source recurrence, average graphemic length, positional tendencies, and strongest structural candidates.

Genre/domain metadata may describe the document class, but it may not be used to force grammatical interpretations.

## 6. Language graph

Graph node types:

- `SOURCE`
- `FORM`
- `EDGE_MATERIAL_PATTERN`

Graph edge types:

- `SOURCE_ATTESTS_FORM`
- `FORM_NEIGHBOR_FORM`
- `FORM_EDGE_EXTENSION_FORM`
- `PATTERN_SUPPORTED_BY_SOURCE`

Every graph edge must have recoverable evidence fields. Graph topology is an evidence representation, not a claim of linguistic ontology.

## 7. Contamination controls

- Numeric-only forms excluded from linguistic candidate scoring but preserved in the dictionary layer.
- Repeated-template-risk forms from Comparative Research V1 remain flagged.
- Stage-4 claims rejected by independent audit are not used as proof.
- English, Turkish, Arabic, names, metadata, URLs, or other-language strings are not automatically assigned to any language; membership remains unresolved unless separately established.
- No cross-source identical spelling is automatically a shared lemma.

## 8. Required outputs

The builder must produce exhaustive or threshold-declared machine-readable tables plus an integrated report that explicitly separates mechanically established results, strong candidates, weak candidates, unresolved questions, and interpretations not yet licensed.

## 9. Scope limit

V1 builds a structural evidence model from lexicon-level neighbor and position profiles. Full unrestricted sequence grammar over all 47.6M occurrences is a later V2 operation. V1 must state this limit explicitly rather than imply complete grammar reconstruction.
