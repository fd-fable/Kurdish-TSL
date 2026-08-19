# Kurdish-TSL — Exhaustive Corpus-Specific Deep Dictionaries V1

**Method:** `Research_Methods/Dictionary_V1/TSLK_DEEP_DICTIONARY_PROTOCOL_V1.md`

**Corpus-local surface-form entries:** 487,041
**Word-like occurrences represented by the builds:** 47,629,049
**All 14 non-whitespace coverage checks:** PASS

> These are corpus-local evidence entries, not a merged count of unique Kurdish lemmas. Identical spellings in different corpora and spelling variants remain independent evidence.

| Corpus | Surface types | Word-like occurrences | Raw token types | Coverage | Status |
|---|---:|---:|---:|---:|---|
| `001_MEM_U_ZIN` | 3,932 | 7,813 | 4,319 | 39346/39346 | MECHANICALLY COMPLETE / INTERPRETATION UNREVIEWED |
| `002_ANHA` | 71,523 | 28,275,212 | 92,044 | 137188942/137188942 | MECHANICALLY COMPLETE / INTERPRETATION UNREVIEWED |
| `003_RONAHI` | 84,532 | 1,977,137 | 108,571 | 10102098/10102098 | MECHANICALLY COMPLETE / INTERPRETATION UNREVIEWED |
| `004_RUDAW` | 314,182 | 17,311,859 | 446,208 | 84707765/84707765 | MECHANICALLY COMPLETE / INTERPRETATION UNREVIEWED |
| `005_PIRTUKEN_KURMANCI_KATALOG` | 505 | 1,617 | 600 | 8026/8026 | MECHANICALLY COMPLETE / INTERPRETATION UNREVIEWED |
| `006_KURMANJI_BEGINNERS` | 11,740 | 54,650 | 16,769 | 246897/246897 | MECHANICALLY COMPLETE / INTERPRETATION UNREVIEWED |
| `007_KOVARA_KURMANCI` | 85 | 105 | 88 | 700/700 | MECHANICALLY COMPLETE / INTERPRETATION UNREVIEWED |
| `008_KOVARA_HAWAR` | 81 | 100 | 87 | 633/633 | MECHANICALLY COMPLETE / INTERPRETATION UNREVIEWED |
| `009_ROJNAMA_KURDISTAN` | 86 | 104 | 89 | 634/634 | MECHANICALLY COMPLETE / INTERPRETATION UNREVIEWED |
| `010_KOVARA_JIN` | 79 | 93 | 82 | 592/592 | MECHANICALLY COMPLETE / INTERPRETATION UNREVIEWED |
| `011_FOLKLORA_KURMANCA_1936` | 80 | 97 | 85 | 611/611 | MECHANICALLY COMPLETE / INTERPRETATION UNREVIEWED |
| `012_KURD_TEAVUN_TERAKKI_1908` | 70 | 81 | 72 | 510/510 | MECHANICALLY COMPLETE / INTERPRETATION UNREVIEWED |
| `013_ROJI_KURD_1913` | 69 | 88 | 72 | 521/521 | MECHANICALLY COMPLETE / INTERPRETATION UNREVIEWED |
| `014_DIROK_U_CIVAKA_KURDAN` | 77 | 93 | 82 | 562/562 | MECHANICALLY COMPLETE / INTERPRETATION UNREVIEWED |

## What is in Git

- exhaustive sharded `LEXICON_*.tsv` and `LEXICON_*.jsonl` tables for every exact word-like surface form;
- complete raw-token inventory;
- complete character inventory;
- per-corpus manifest with source and builder hashes;
- per-entry frequency, locators, first context, positional counts, neighbor profiles, and graphemic details;
- semantics and grammatical interpretation deliberately unresolved by the mechanical build.

## Full occurrence evidence

The complete 47.6M-occurrence concordance is stored directly in this GitHub repository as compressed per-corpus shards under `Dictionaries/<CORPUS>/Occurrences/OCCURRENCES_*.tsv.gz`. The Actions artifact remains as a backup. Large lexicons remain row-sharded so every ordinary Git file stays below GitHub file-size limits.
