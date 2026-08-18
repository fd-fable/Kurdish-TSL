# Kurdish-TSL — Deep Dictionary V1 Build Audit

## Status

**MECHANICAL EXHAUSTIVE VOCABULARY BUILD: COMPLETE FOR ALL 14 COMMITTED CSTLK CORPORA**

This audit records the completed first-layer deep dictionary build under:

`Research_Methods/Dictionary_V1/TSLK_DEEP_DICTIONARY_PROTOCOL_V1.md`

The dictionary packages are committed under:

`Dictionaries/`

Merge commit:

`02a8e9026025888c4c0623110c2ebfa80e3e9cbe`

---

## 1. Scope

The build indexes the vocabulary actually present in each committed `CSTLK*.docx` corpus representation.

The fourteen corpora remain isolated. Identical spellings in different corpora are independent evidence entries during this stage.

The mechanical build does not:

- translate forms;
- assign lemmas;
- assign grammatical categories;
- infer morpheme boundaries;
- normalize toward standard Kurdish;
- merge historical/spelling variants;
- transfer meanings or analyses between corpora.

Every generated lexical entry therefore begins with semantic and interpretive status unresolved.

---

## 2. Project-wide verified counts

- **Corpus-local exact word-like surface-form entries:** `487,041`
- **Word-like occurrences represented by the complete evidence builds:** `47,629,049`
- **Numbered corpora completed:** `14/14`
- **Non-whitespace character coverage audits:** `14/14 PASS`
- **Cross-corpus lemma merging:** `NONE`
- **Semantic assignment by mechanical builder:** `NONE`
- **Grammatical classification by mechanical builder:** `NONE`

`487,041` is not a claim that Kurdish has 487,041 unique lemmas. It is the sum of independently preserved corpus-local exact surface-form inventories. Duplicate forms across corpora and distinct spelling/case/diacritic variants remain separate evidence.

---

## 3. Per-corpus inventory

| Corpus | Layer-W surface types | Layer-W occurrences | Raw token types | Non-whitespace coverage | Build status |
|---|---:|---:|---:|---:|---|
| `001_MEM_U_ZIN` | 3,932 | 7,813 | 4,319 | 39,346/39,346 | PASS |
| `002_ANHA` | 71,523 | 28,275,212 | 92,044 | 137,188,942/137,188,942 | PASS |
| `003_RONAHI` | 84,532 | 1,977,137 | 108,571 | 10,102,098/10,102,098 | PASS |
| `004_RUDAW` | 314,182 | 17,311,859 | 446,208 | 84,707,765/84,707,765 | PASS |
| `005_PIRTUKEN_KURMANCI_KATALOG` | 505 | 1,617 | 600 | 8,026/8,026 | PASS |
| `006_KURMANJI_BEGINNERS` | 11,740 | 54,650 | 16,769 | 246,897/246,897 | PASS |
| `007_KOVARA_KURMANCI` | 85 | 105 | 88 | 700/700 | PASS |
| `008_KOVARA_HAWAR` | 81 | 100 | 87 | 633/633 | PASS |
| `009_ROJNAMA_KURDISTAN` | 86 | 104 | 89 | 634/634 | PASS |
| `010_KOVARA_JIN` | 79 | 93 | 82 | 592/592 | PASS |
| `011_FOLKLORA_KURMANCA_1936` | 80 | 97 | 85 | 611/611 | PASS |
| `012_KURD_TEAVUN_TERAKKI_1908` | 70 | 81 | 72 | 510/510 | PASS |
| `013_ROJI_KURD_1913` | 69 | 88 | 72 | 521/521 | PASS |
| `014_DIROK_U_CIVAKA_KURDAN` | 77 | 93 | 82 | 562/562 | PASS |

The small inventories for Corpora 007–014 reflect the currently committed CSTLK representations. They must not be interpreted as the full historical source sizes. Future expansion of a CSTLK corpus will require a new dictionary build/version.

---

## 4. Exhaustiveness architecture

Two inventories are retained for every corpus.

### Layer R — raw written-token inventory

Whitespace-delimited source strings are retained exactly, including punctuation attachment and unusual forms. This is an audit/completeness layer and does not claim linguistic word boundaries.

### Layer W — mechanical word-like surface inventory

Unicode letter/mark/number sequences are indexed under the explicit mechanical tokenizer in the protocol. This creates searchable dictionary entries while making no linguistic segmentation claim.

Every Layer-W entry includes evidence fields such as:

- exact surface form;
- deterministic entry ID;
- technical NFC/casefold search keys;
- frequency;
- source-document part;
- first/last/sample locators;
- first attested context;
- container-initial/final counts;
- immediate left/right neighbor profiles;
- character sequence and graphemic edge information;
- unresolved semantic/interpretive status.

---

## 5. Repository storage design

The first aggregate attempt assembled approximately `1.8 GB` of dictionary + complete occurrence evidence. GitHub correctly rejected the ordinary Git push because:

- `004_RUDAW/LEXICON.tsv` was about `126.91 MB`;
- `004_RUDAW/LEXICON.jsonl` was about `299.77 MB`;
- GitHub ordinary Git files cannot exceed `100 MB`.

This was a storage failure only. All fourteen corpus builds had already passed completeness checks.

The accepted repository-safe build therefore:

1. preserves **every vocabulary entry** in Git;
2. shards large TSV/JSONL lexicons into files of at most 50,000 entries;
3. verifies sharded TSV row count = original surface-type count;
4. verifies sharded JSONL row count = original surface-type count;
5. commits raw-token and character inventories plus corpus manifests;
6. keeps the complete 47.6-million-occurrence concordance evidence outside ordinary Git as a cryptographically identified GitHub Actions artifact.

No vocabulary entry is omitted by this storage separation.

---

## 6. Full concordance evidence archive

Repository-safe publisher workflow run:

`32168308087`

Long-retention evidence artifact:

- **Artifact name:** `TSLK_DEEP_DICTIONARY_FULL_EVIDENCE_V1`
- **Artifact ID:** `9336377934`
- **Size:** `1,872,421,234 bytes`
- **SHA-256:** `d86e1c34f8af36b7d66dfd5479152f32ef12ae6d8f88e2665a73c6e6cbd9ea66`
- **Created:** `2026-08-18T18:00:18Z`
- **Expires:** `2026-11-16T17:56:43Z`
- **Expired at audit time:** `false`

The archive contains the complete per-corpus build packages including occurrence/concordance shards. Per-corpus manifests in Git also identify the original validated matrix-build artifact IDs and digests.

Because GitHub Actions artifacts are retention-bound, the repository manifests and source/builder hashes remain the durable reconstruction mechanism even after artifact expiry. The dictionaries are deterministically rebuildable from committed CSTLK files and the committed builder.

---

## 7. Reproducibility

Builder:

`Research_Methods/Dictionary_V1/tools/build_deep_dictionaries.py`

Builder version:

`TSLK_DEEP_DICTIONARY_BUILDER_V1.0.0`

Builder SHA-256 used for the validated matrix build:

`c979a031e7651da908f6dd6c9ca23a7d67d9d6bbb1bb64bcf880352ec4e05865`

Validated matrix-build run:

`32165597134`

Repository-safe publisher run:

`32168308087`

The first large aggregate Git push failed only at GitHub's file-size gate; the subsequent sharded publisher completed successfully and the resulting dictionary core was merged to `main`.

---

## 8. Current evidential status

The dictionary stage now has two distinct states:

### Mechanically established

- exact written-form attestation;
- frequency;
- mechanical context/neighbor distribution;
- graphemic representation;
- corpus-local positional metadata;
- complete raw token inventory;
- complete character coverage;
- source/build provenance.

### Not yet established by the dictionary build

- lexical meaning;
- pronunciation;
- lemma identity;
- grammatical category;
- morphological segmentation;
- etymology;
- historical relationship;
- equivalence across corpora.

Those belong to later evidence-based enrichment layers and must not be silently imported from existing Kurdish knowledge.

---

## 9. Next dictionary research layer

The exhaustive V1 inventory is the substrate for a later **Deep Lexical Interpretation Layer**, where entries can be enriched from internal corpus evidence with:

- distributional frames;
- recurring construction participation;
- form-family hypotheses;
- contextual semantic hypotheses;
- competing interpretations;
- counterexamples;
- confidence/status;
- explicit unresolved questions;
- later, separately sourced native-speaker evidence.

That interpretive layer must be versioned separately and must never overwrite the mechanical evidence inventory.
