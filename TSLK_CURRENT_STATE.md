# Kurdish-TSL — Current Project State

## Active milestone

**Sciences of Language V2 full-occurrence structural reconstruction is COMPLETE and merged into `main`.**

V2 merge commit:

`dae3aa2cd3e943a1475d4f3244dc7974d0610c31`

Active V2 report:

`Sciences_of_Language_V2/TSLK_SCIENCES_OF_LANGUAGE_REPORT_V2.md`

V2 manifest:

`Sciences_of_Language_V2/SCIENCES_OF_LANGUAGE_V2_MANIFEST.json`

V2 build audit:

`Sciences_of_Language_V2/TSLK_SCIENCES_OF_LANGUAGE_AUDIT_V2.md`

Full source-pattern repository manifest:

`Sciences_of_Language_V2/FULL_PATTERN_REPOSITORY_MANIFEST.json`

## V2 verified coverage

- Named sources: **14**
- Expected occurrence rows: **47,629,049**
- Scanned occurrence rows: **47,629,049**
- Full occurrence coverage: **PASS**
- Active structural-candidate occurrences: **43,486,547**
- Preserved documentary/technical-risk occurrences outside active structural scoring: **4,142,502**
- Ordering anomalies: **0** in all source audits
- Complete source-local recurrent-pattern tables committed directly to GitHub: **84/84**
- Six full pattern families per source: BIGRAMS, TRIGRAMS, FOURGRAMS, SLOT_FRAMES, GAP2, GAP3
- All committed full pattern tables passed gzip integrity checks and Git-size checks.

## V2 cross-source structural results

Cross-source retained patterns after source-local recurrence thresholds:

- BIGRAMS: **173,399**
- TRIGRAMS: **147,070**
- FOURGRAMS: **74,054**
- SLOT_FRAMES: **60,552**
- GAP2: **176,712**
- GAP3: **158,980**

Full-context V1 morphology-family candidates surviving the V2 cross-source threshold: **9,717**.

Cross-source full-occurrence position profiles: **54,628**.

Language Graph V2 high-evidence core:

- nodes: **17,085**
- edges: **21,161**

These counts describe retained evidence objects, not a count of grammatical rules.

## Example high-evidence V2 structures

Examples currently ranked highly by complete occurrence evidence include:

- `li ser`
- `ji bo`
- `kir ku`
- `ji ber ku`
- `bi hev re`
- `Di heman demê de`
- `Ji ber vê yekê`
- `di + SLOT + de`
- `bi + SLOT + re`
- `ji + SLOT + re`
- `di _ _ de`
- `di _ _ _ de`

These remain **STRUCTURAL / CONSTRUCTION CANDIDATES**. V2 does not automatically assign conventional grammatical functions to them.

## Morphology status

V2 re-tested high-ranked V1 form-family candidates against complete occurrence contexts. Examples of surviving written-family relations include relations such as `a → ya`, `nav → nava`, `e → ye`, `gor → gorî`, `hatin → hatine`, `hat → hatiye`, `yê → yên`, and `kir → kirin`.

These remain **FORM-FAMILY / MORPHOLOGY CANDIDATES**. Similar written shape plus contextual support does not by itself prove prefix, suffix, inflection, derivation, tense, case, agreement, or any other conventional category.

## V2 evidence storage

All complete source-local V2 pattern evidence is repository-resident at:

`Sciences_of_Language_V2/Per_Source/<CORPUS>/Patterns/`

Every one of the 84 tables has exact row counts, compressed size, SHA-256 digest, and gzip-integrity status in:

`Sciences_of_Language_V2/FULL_PATTERN_REPOSITORY_MANIFEST.json`

GitHub Actions artifacts are not required for future access to the complete V2 pattern evidence.

## Active evidence hierarchy

1. `Sources/` material — primary source evidence
2. `CSTLK...` corpora — corpus evidence, source fidelity subject to audit
3. Deep Dictionary V1 — exhaustive mechanical vocabulary and occurrence evidence
4. Comparative Research V1 — named-source convergence without source collapse
5. Sciences of Language V1 — lexicon-level structural skeleton
6. **Sciences of Language V2 — active full-occurrence structural reconstruction layer**
7. Earlier agent Stage-4 DSR/self-certified grammar outputs — preserved research history, not active proof

## Earlier completed milestones

Deep Dictionary V1:

- vocabulary-core merge: `02a8e9026025888c4c0623110c2ebfa80e3e9cbe`
- full repository occurrence evidence merge: `a9e9bd7cb1cf43e3f01d75330ed67d01a2be42d2`
- 487,041 corpus-local exact surface entries
- 47,629,049 word-like occurrences
- 250/250 occurrence shards stored directly in GitHub

Comparative Research V1:

- merge: `42b2b71e269272a6acd0ae291abea867a71d04ae`
- 278,875 letter-bearing/no-numeric exact-form union
- 54,774 letter-bearing forms shared by at least two named sources
- 54,762 shared candidates after the current repeated-context risk flag

Sciences of Language V1:

- merge: `6b859a02482ee53a1e528a73d9b527a52b6dfea5`
- 405,177 written form-family candidates
- 26,291 recurring edge-material patterns
- 66,844 immediate-neighbor structural candidates
- 55,276 V1 graph nodes / 284,344 V1 graph edges

## Epistemic status after V2

Mechanically/structurally established:

- exhaustive occurrence-row coverage;
- exact source-local and cross-source recurrent sequences under declared thresholds;
- exact variable-slot frames;
- exact gap-2 and gap-3 endpoint relations;
- full candidate-stream position profiles;
- complete immediate-context tests for selected V1 form-family candidates;
- source incidence and source-distribution evidence;
- documentary/technical-risk accounting;
- provenance-preserving construction and form-family graph evidence.

Not automatically established:

- final lexical meaning;
- pronunciation/phonology from text alone;
- final lemma identity;
- definitive morphemes, affixes, or segmentation;
- noun/verb/adjective classes;
- subject/object relations;
- tense/aspect/mood categories;
- case/ergativity systems;
- semantic or grammatical identity of same-spelled forms across sources;
- language membership for every mechanically retained letter-bearing item.

All V2 evidence scores are ranking measures, **not probabilities of grammatical truth**.

## Historical-source limitation

The committed CSTLK slices for several sources 007–014 remain very small. Their V2 patterns are valid for the committed slices, but they must not be generalized to the complete historical works or traditions until those corpora are expanded from their preserved `Sources/` material.

## Research-stream isolation

Stream A documentary/corpus analysis remains isolated from Stream B Ferhad/native-speaker evidence until an explicitly authorized convergence phase. V2 did not use Stream B.

## Next valid research stage

The next stage is **evidence-backed interpretive reconstruction** rather than another blind counting layer:

1. select the strongest V2 constructions and form-family candidates;
2. retrieve their complete source-local support and counterexamples;
3. test competing structural analyses;
4. discover constituent/slot classes from distribution rather than inherited labels;
5. build contradiction and exception registers;
6. propose conventional morphology/grammar terminology only where it explains and predicts the corpus better than neutral alternatives;
7. expand underrepresented historical CSTLK corpora and re-test conclusions;
8. only later begin documentary-vs-native-speaker convergence.

## New-chat continuation rule

For future project chats, inspect `TSLK_PROJECT_CONTEXT.md`, this file, `Comparative_Research_V1/README.md`, `Sciences_of_Language_V1/README.md`, and `Sciences_of_Language_V2/README.md`. GitHub is the durable source of truth; Ferhad should not need to copy prior project history.
