# Kurdish-TSL — Current Project State

## Current milestone

**Deep Dictionary V1 is mechanically complete for all 14 committed CSTLK corpora, the complete occurrence evidence is repository-resident, and Comparative Research V1 now connects the named sources without erasing their independence.**

Vocabulary-core merge commit:

`02a8e9026025888c4c0623110c2ebfa80e3e9cbe`

Complete repository-evidence merge commit:

`a9e9bd7cb1cf43e3f01d75330ed67d01a2be42d2`

Named-source comparative merge commit:

`42b2b71e269272a6acd0ae291abea867a71d04ae`

## Active named-source comparative structure

The active combined report is:

`Comparative_Research_V1/TSLK_COMBINED_NAMED_SOURCE_RESEARCH_V1_FINAL.md`

Its required hierarchy is:

1. Mem û Zîn — source-specific research/evidence
2. ANHA — source-specific research/evidence
3. Ronahî — source-specific research/evidence
4. Rudaw — source-specific research/evidence
5. Pirtûkên Kurmancî Katalog — source-specific research/evidence
6. Kurmanji Beginners — source-specific research/evidence
7. Kovara Kurmancî — source-specific research/evidence
8. Kovara Hawar — source-specific research/evidence
9. Rojnama Kurdistan — source-specific research/evidence
10. Kovara Jîn — source-specific research/evidence
11. Folklora Kurmanca (1936) — source-specific research/evidence
12. Kurd Teavun Terakki (1908) — source-specific research/evidence
13. Rojî Kurd (1913) — source-specific research/evidence
14. Dîrok û Civaka Kurdan — source-specific research/evidence
15. cross-source comparison
16. final combined result
17. deep conclusion

This convergence layer is non-destructive. The original `001_...` through `014_...` directories remain the source-specific evidence systems.

## Verified comparative totals

Documentary/all-mechanical layer:

- corpus-local surface entries before convergence: **487,041**
- global exact-surface documentary union: **380,145**
- exact forms shared by at least two sources: **67,485**
- exact forms shared by all fourteen sources: **9**

Audited lexical-candidate layer:

- letter-bearing/no-numeric exact-form union: **278,875**
- letter-bearing exact forms shared by at least two named sources: **54,774**
- letter-bearing exact forms occurring in all fourteen named sources: **6**
- repeated-identical-first-context template-risk forms: **12**
- shared ≥2-source letter-bearing candidates after excluding that risk flag: **54,762**

Language membership remains unresolved in this layer. The filter removes numeric forms and flags repeated context reuse, but it does not automatically declare a written form Kurdish or non-Kurdish.

## Comparative machine-readable evidence

- `Comparative_Research_V1/Data/EXACT_SURFACE_CROSS_SOURCE_INDEX.tsv.gz`
- `Comparative_Research_V1/Data/LETTER_BEARING_CROSS_SOURCE_INDEX.tsv.gz`
- `Comparative_Research_V1/Data/SOURCE_COMPARATIVE_SUMMARY.tsv`
- `Comparative_Research_V1/Data/SOURCE_LETTER_BEARING_SUMMARY.tsv`
- `Comparative_Research_V1/Data/PAIRWISE_EXACT_SURFACE_COMPARISON.tsv`
- `Comparative_Research_V1/Data/PAIRWISE_LETTER_BEARING_COMPARISON.tsv`
- `Comparative_Research_V1/COMPARATIVE_BUILD_MANIFEST.json`
- `Comparative_Research_V1/COMPARATIVE_AUDIT_MANIFEST.json`

The comparison builders are preserved under `Comparative_Research_V1/tools/` for reproducibility.

## Dictionary evidence

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

Verified dictionary totals:

- 14/14 corpus dictionaries mechanically complete.
- 487,041 corpus-local exact word-like surface-form entries.
- 47,629,049 represented word-like occurrences.
- 250/250 compressed occurrence/concordance shards physically committed to GitHub.
- 14/14 non-whitespace character coverage checks passed.
- No cross-corpus lemma merging by the dictionary builder.
- No external semantic assignment.
- No grammatical classification by the builder.

The 487,041 figure is not a global Kurdish lemma count. It intentionally preserves duplicate forms across corpora and spelling/case/diacritic variants as independent evidence.

## Evidence storage

Git contains the complete vocabulary core for every corpus, including sharded exhaustive TSV/JSONL lexicons, raw-token inventories, character inventories, per-corpus manifests, frequencies, locators, contexts, positional counts, immediate-neighbor profiles, and graphemic metadata.

The complete 47.6-million-occurrence concordance evidence is also stored directly in the repository as **250 compressed shards** under:

`Dictionaries/<CORPUS>/Occurrences/OCCURRENCES_*.tsv.gz`

Final remote verification on the publication branch returned:

`FINAL REMOTE PASS: 250 occurrence shards physically present on safety branch.`

Those verified objects were merged into `main` in commit `a9e9bd7cb1cf43e3f01d75330ed67d01a2be42d2`. The master manifest records `all_occurrence_shards_committed_to_git: true`.

The GitHub Actions artifact remains as an independent backup copy:

- name: `TSLK_DEEP_DICTIONARY_FULL_EVIDENCE_V1`
- artifact ID: `9336377934`
- size: `1,872,421,234 bytes`
- SHA-256: `d86e1c34f8af36b7d66dfd5479152f32ef12ae6d8f88e2665a73c6e6cbd9ea66`
- source publisher run: `32168308087`
- expires: `2026-11-16T17:56:43Z`

The evidence is therefore available directly through GitHub and is also deterministically rebuildable from the committed CSTLK files, builder, and source hashes.

## Epistemic status

Mechanically established:

- exact written-form attestation;
- exact surface spelling;
- source-specific frequency;
- character/grapheme representation;
- source/document locators;
- first attested context;
- local positional distribution;
- immediate left/right neighbor profiles;
- complete occurrence/concordance evidence;
- cross-source exact-form membership;
- pairwise exact-form overlap;
- letter-bearing/no-numeric candidate membership;
- repeated-identical-first-context template-risk flags;
- source/build provenance.

Not yet established by these mechanical/comparative layers:

- lexical meaning;
- pronunciation;
- lemma identity;
- language membership for every extracted form;
- grammatical category;
- morphological segmentation;
- etymology;
- semantic equivalence across corpora;
- grammatical equivalence across corpora.

These must be added only in separately versioned evidence-based enrichment layers. Existing Kurdish dictionaries/grammar or remembered Kurdish-specific rules remain inadmissible as blind-discovery evidence.

## Stage 4 status remains separate

The external-agent Stage 4 V1 grammar/discovery certification remains rejected by independent audit. See:

`Research_Methods/Stage4_V1/TSLK_INDEPENDENT_AUDIT_FINDINGS.md`

The combined dictionary/comparative work does not rehabilitate those failed grammatical analyses.

## Research streams

Stream A documentary/corpus analysis remains isolated from Stream B Ferhad/native-speaker evidence until an explicitly authorized later comparison phase.

## Next research layer

The next valid interpretive unit is the **cross-source candidate bundle**:

`exact form + named-source membership + source-specific frequency + source-specific contexts + template-risk status`

For high-value recurrent candidates, analyze contextual behavior independently inside each named source before proposing shared meaning, lemma identity, morphology, or grammatical function. Agreement across independently analyzed sources may raise confidence; disagreement must remain visible as evidence rather than being normalized away.

## New-chat continuation rule

When continuing this project in another chat, inspect `TSLK_PROJECT_CONTEXT.md`, this file, and `Comparative_Research_V1/README.md` before asking Ferhad to restate project history. GitHub is the durable source of truth for current project state.
