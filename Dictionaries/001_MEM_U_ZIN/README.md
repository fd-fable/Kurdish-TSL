# Deep Dictionary — 001_MEM_U_ZIN

**Status:** MECHANICALLY COMPLETE / INTERPRETATION UNREVIEWED

**Source CSTLK:** `001_MEM_U_ZIN/CSTLK001MEMUZIN08172026FDA.docx`  
**Source SHA-256:** `6d2b7b83c00b5b11ca030ca1aab87cd5b1051fd83d0d7e9690fb268bbd7024f3`  
**Builder:** `TSLK_DEEP_DICTIONARY_BUILDER_V1.0.0`  
**Builder SHA-256:** `c979a031e7651da908f6dd6c9ca23a7d67d9d6bbb1bb64bcf880352ec4e05865`

## Exhaustive inventory

- Layer R raw written-token occurrences: **7,931**
- Layer R distinct raw written-token types: **4,319**
- Layer W mechanical word-like occurrences: **7,813**
- Layer W distinct exact surface forms: **3,932**
- Text containers processed: **357**
- Non-whitespace character coverage: **39,346/39,346**

## Files

- `LEXICON.tsv` — exhaustive unique Layer W dictionary entries.
- `LEXICON.jsonl` — machine-readable equivalent.
- `RAW_TOKEN_INVENTORY.tsv` — exact whitespace-token inventory preserving punctuation attachment.
- `CHARACTER_INVENTORY.tsv` — complete extracted character inventory.
- `OCCURRENCES_*.tsv.gz` — complete concordance/occurrence stream in shards.
- `MANIFEST.json` — hashes, counts, audit checks, and build provenance.

## Interpretation rule

Every generated entry begins with:

`SEMANTIC VALUE UNRESOLVED`

`INTERPRETATION UNREVIEWED`

`CORPUS-SCOPE UNREVIEWED`

This package does not import external Kurdish meanings, grammar, lemmas, or cross-corpus equivalences. The exact surface form is evidence; technical NFC/casefold fields are search aids only.

## Completeness checks

- Non-whitespace character coverage: **PASS**
- Layer W frequency sum: **PASS**
- Layer R frequency sum: **PASS**

See `Research_Methods/Dictionary_V1/TSLK_DEEP_DICTIONARY_PROTOCOL_V1.md`.

## Repository storage

The exhaustive vocabulary tables are sharded in Git. The complete occurrence/concordance stream is preserved in the validated GitHub Actions evidence artifact referenced in `MANIFEST.json`; this separation is storage-only and does not drop any vocabulary entry.
