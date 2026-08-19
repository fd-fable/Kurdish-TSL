# Kurdish-TSL — Current Project State

## Current milestone

**The project now has four active evidence layers:**

1. source-specific CSTLK corpora;
2. Deep Dictionary V1;
3. Comparative Research V1;
4. **Sciences of Language V1 structural model**.

Sciences of Language V1 merge commit:

`6b859a02482ee53a1e528a73d9b527a52b6dfea5`

Active report:

`Sciences_of_Language_V1/TSLK_SCIENCES_OF_LANGUAGE_REPORT_V1.md`

Protocol:

`Sciences_of_Language_V1/TSLK_SCIENCES_OF_LANGUAGE_PROTOCOL_V1.md`

Scope audit:

`Sciences_of_Language_V1/TSLK_SCIENCES_OF_LANGUAGE_AUDIT_V1.md`

Manifest:

`Sciences_of_Language_V1/SCIENCES_OF_LANGUAGE_MANIFEST.json`

## Sciences of Language V1 verified outputs

- 14 named sources represented.
- 54,762 shared non-template-risk letter-bearing form profiles.
- 405,177 exact graphemic edge-extension / form-family candidates.
- 26,291 recurring edge-material patterns.
- 66,844 cross-source immediate-neighbor structural candidates.
- 54,762 positional candidate profiles.
- 55,276 language-graph nodes.
- 284,344 language-graph edges.

Evidence tables:

- `Sciences_of_Language_V1/Data/SOURCE_LANGUAGE_SCIENCE_PROFILE.tsv`
- `Sciences_of_Language_V1/Data/FORM_STRUCTURE_PROFILE.tsv.gz`
- `Sciences_of_Language_V1/Data/FORM_FAMILY_CANDIDATES.tsv.gz`
- `Sciences_of_Language_V1/Data/EDGE_MATERIAL_PATTERNS.tsv`
- `Sciences_of_Language_V1/Data/STRUCTURAL_NEIGHBOR_CANDIDATES.tsv.gz`
- `Sciences_of_Language_V1/Data/POSITIONAL_CANDIDATES.tsv.gz`
- `Sciences_of_Language_V1/Data/LITERATURE_REGISTER_PROFILE.tsv`

Language graph:

- `Sciences_of_Language_V1/Graph/LANGUAGE_GRAPH_NODES.tsv.gz`
- `Sciences_of_Language_V1/Graph/LANGUAGE_GRAPH_EDGES.tsv.gz`
- `Sciences_of_Language_V1/Graph/LANGUAGE_GRAPH_CORE.graphml.gz`

## Current morphology result

The project has not declared definitive morphemes. It has built an evidence-ranked graphemic morphology-candidate system.

Highest recurring edge-material candidates currently include right-edge `ê`, `n`, `a`, `an`, `î`, `ên`, `e`, `yê`, `in`, `ek` and left-edge materials including `y`, `d`, `di`, `v`, `w`, `nav`, `bi`, `ne`, etc.

These are **EDGE-MATERIAL PATTERNS / FUNCTION UNRESOLVED**. They must be checked against complete source-local contexts before promotion to morphological hypotheses.

## Current structural / grammar result

V1 generated 66,844 cross-source immediate-neighbor candidates. Strong evidence-ranked examples include exact written relations such as:

- `li → ser`
- `ji → bo`
- `kir → ku`
- `ku → li`
- `di → navbera`
- `ji → ber`
- `ku → di`
- `di → nav`
- `li → dijî`
- `li → ber`

These are **STRUCTURAL NEIGHBOR CANDIDATES / RELATION UNRESOLVED**. They are distributional facts from the current lexicon neighbor profiles, not automatically syntactic dependencies or conventional grammatical constructions.

## Evidence scores

Sciences of Language V1 defines evidence-ranking scores, not correctness probabilities.

- **SES — Structural Evidence Score:** source diversity + normalized support + source-distribution entropy.
- **FFES — Form-Family Evidence Score:** source diversity + normalized support + observed neighbor-context similarity.

A high score means a pattern is independently recurrent and worth deeper testing. It does not mean a grammar rule is proven.

## Literature / register status

Each named source now has its own quantitative profile including type/token relation, one-occurrence-form share, cross-source recurrence, weighted graphemic length, and positional evidence.

The currently committed corpora are highly unequal in depth. ANHA, Ronahî, Rudaw, Kurmanji Beginners, and Mem û Zîn provide substantially deeper evidence. Sources 007–014 currently contain only small CSTLK slices with tens of letter-bearing types; their statistics describe the committed slices and must not be generalized to the complete historical works or traditions.

## Language graph status

The project now has a real provenance-preserving evidence graph.

Node types:

- `SOURCE`
- `FORM`
- `EDGE_MATERIAL_PATTERN`

Edge types:

- `SOURCE_ATTESTS_FORM`
- `FORM_NEIGHBOR_FORM`
- `FORM_EDGE_EXTENSION_FORM`

Graph communities or clusters are not automatically grammatical categories.

## Comparative Research V1

Named-source comparative merge commit:

`42b2b71e269272a6acd0ae291abea867a71d04ae`

Active combined report:

`Comparative_Research_V1/TSLK_COMBINED_NAMED_SOURCE_RESEARCH_V1_FINAL.md`

Required hierarchy:

1. Mem û Zîn
2. ANHA
3. Ronahî
4. Rudaw
5. Pirtûkên Kurmancî Katalog
6. Kurmanji Beginners
7. Kovara Kurmancî
8. Kovara Hawar
9. Rojnama Kurdistan
10. Kovara Jîn
11. Folklora Kurmanca (1936)
12. Kurd Teavun Terakki (1908)
13. Rojî Kurd (1913)
14. Dîrok û Civaka Kurdan
15. cross-source comparison
16. final combined result
17. deep conclusion

Verified comparative totals:

- corpus-local surface entries before convergence: 487,041
- global exact-surface documentary union: 380,145
- letter-bearing/no-numeric exact-form union: 278,875
- letter-bearing forms shared by at least two named sources: 54,774
- repeated-identical-first-context template-risk forms: 12
- shared ≥2-source candidates after that risk flag: 54,762

## Deep Dictionary V1

Vocabulary-core merge commit:

`02a8e9026025888c4c0623110c2ebfa80e3e9cbe`

Complete repository-evidence merge commit:

`a9e9bd7cb1cf43e3f01d75330ed67d01a2be42d2`

Verified totals:

- 14/14 corpus dictionaries mechanically complete.
- 487,041 corpus-local exact word-like surface-form entries.
- 47,629,049 represented word-like occurrences.
- 250/250 compressed occurrence/concordance shards physically committed to GitHub.
- 14/14 non-whitespace character coverage checks passed.

The complete occurrence evidence lives under:

`Dictionaries/<CORPUS>/Occurrences/OCCURRENCES_*.tsv.gz`

## Epistemic status

Mechanically/structurally established now:

- exact written-form attestation and source incidence;
- source-specific and cross-source frequency;
- graphemic representation;
- local neighbor recurrence;
- position counts;
- graphemic edge-extension relations;
- recurrent edge-material patterns;
- ranked cross-source neighbor relations;
- literature/register quantitative differences for the committed corpus slices;
- graph topology of source, form, adjacency, and edge-extension evidence.

Not yet established:

- definitive lexical meanings for all forms;
- pronunciation or phonology from text alone;
- final lemma identity;
- definitive morphemes/affixes;
- noun/verb/adjective classes;
- subject/object relations;
- tense/aspect/mood categories;
- case/ergativity systems;
- complete grammar over all 47.6M occurrences;
- semantic or grammatical equivalence across corpora.

## Stage 4 status

The external-agent Stage 4 V1 grammar/discovery certification remains rejected by independent audit:

`Research_Methods/Stage4_V1/TSLK_INDEPENDENT_AUDIT_FINDINGS.md`

Dictionary, comparative, and Sciences of Language V1 outputs do not rehabilitate those failed claims.

## Research-stream isolation

Stream A documentary/corpus analysis remains isolated from Stream B Ferhad/native-speaker evidence until an explicitly authorized later convergence phase.

## Next research layer — Sciences of Language V2

V2 should use the complete 47.6-million occurrence stream to test the V1 graph with unrestricted context:

- complete bigram, trigram, and longer recurring sequences;
- discontinuous construction candidates;
- source-local and cross-source positional frames;
- graph communities under complete context rather than top-neighbor truncation;
- every occurrence of high-ranked V1 edge-extension candidates;
- competing segmentation models;
- source/register and historical variation;
- contradiction and exception inventories;
- candidate sentence/construction formulas only after the evidence supports them.

Only after those tests should conventional morphological or grammatical categories be considered for promotion from candidate interpretation to evidence-backed analysis.

## New-chat continuation rule

When continuing this project in another chat, inspect `TSLK_PROJECT_CONTEXT.md`, this file, `Comparative_Research_V1/README.md`, and `Sciences_of_Language_V1/README.md` before asking Ferhad to restate project history. GitHub is the durable source of truth.
