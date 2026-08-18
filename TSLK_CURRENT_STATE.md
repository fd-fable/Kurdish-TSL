# Kurdish-TSL — Current Project State

## Current milestone

**Deep Dictionary V1 mechanical evidence layer is COMPLETE for all 14 committed CSTLK corpora.**

Merged dictionary commit:

`02a8e9026025888c4c0623110c2ebfa80e3e9cbe`

Dictionary index:

`Dictionaries/INDEX.md`

Master dictionary manifest:

`Dictionaries/DICTIONARY_BUILD_MANIFEST.json`

Dictionary protocol:

`Research_Methods/Dictionary_V1/TSLK_DEEP_DICTIONARY_PROTOCOL_V1.md`

Dictionary build audit:

`Research_Methods/Dictionary_V1/TSLK_DICTIONARY_BUILD_AUDIT_V1.md`

Builder:

`Research_Methods/Dictionary_V1/tools/build_deep_dictionaries.py`

## Verified dictionary totals

- 14/14 corpus dictionaries mechanically complete.
- 487,041 corpus-local exact word-like surface-form entries.
- 47,629,049 represented word-like occurrences.
- 14/14 non-whitespace character coverage checks passed.
- No cross-corpus lemma merging.
- No external semantic assignment.
- No grammatical classification by the builder.

The 487,041 figure is not a global Kurdish lemma count. It intentionally preserves duplicate forms across corpora and spelling/case/diacritic variants as independent evidence.

## Evidence storage

Git contains the complete vocabulary core for every corpus, including sharded exhaustive TSV/JSONL lexicons, raw-token inventories, character inventories, per-corpus manifests, frequencies, locators, contexts, positional counts, immediate-neighbor profiles, and graphemic metadata.

The complete 47.6-million-occurrence concordance evidence is preserved as GitHub Actions artifact:

- name: `TSLK_DEEP_DICTIONARY_FULL_EVIDENCE_V1`
- artifact ID: `9336377934`
- size: `1,872,421,234 bytes`
- SHA-256: `d86e1c34f8af36b7d66dfd5479152f32ef12ae6d8f88e2665a73c6e6cbd9ea66`
- source publisher run: `32168308087`
- expires: `2026-11-16T17:56:43Z`

The evidence is deterministically rebuildable after artifact expiry from committed CSTLK files plus the committed builder and per-corpus source hashes.

## Dictionary epistemic status

Mechanically established:

- exact written-form attestation;
- exact surface spelling;
- frequency;
- character/grapheme representation;
- source/document locators;
- first attested context;
- local positional distribution;
- immediate left/right neighbor profiles;
- raw token inventory;
- character inventory;
- source/build provenance.

Not yet established by the mechanical layer:

- lexical meaning;
- pronunciation;
- lemma identity;
- grammatical category;
- morphological segmentation;
- etymology;
- equivalence across corpora.

These must be added only in separately versioned evidence-based enrichment layers. Existing Kurdish dictionaries/grammar or remembered Kurdish-specific rules remain inadmissible as blind-discovery evidence.

## Stage 4 status remains separate

The external-agent Stage 4 V1 grammar/discovery certification remains rejected by independent audit. See:

`Research_Methods/Stage4_V1/TSLK_INDEPENDENT_AUDIT_FINDINGS.md`

Do not treat the dictionary completion as rehabilitation of those failed grammatical analyses.

## Research streams

Stream A documentary/corpus analysis remains isolated from Stream B Ferhad/native-speaker evidence until an explicitly authorized later comparison phase.

## Next lexical research layer

The next dictionary task is the **Deep Lexical Interpretation Layer**. It should enrich the exhaustive entries without deleting or overwriting the mechanical inventory, using corpus-internal evidence to record:

- distributional frames;
- recurring construction participation;
- form-family hypotheses;
- contextual semantic hypotheses;
- competing interpretations;
- counterexamples;
- confidence/status;
- unresolved questions;
- later, separately attributed native-speaker evidence.

All enrichment must remain corpus-specific during first-pass analysis.

## New-chat continuation rule

When continuing this project in another chat, inspect `TSLK_PROJECT_CONTEXT.md` and this file before asking Ferhad to restate project history. GitHub is the durable source of truth for current project state.
