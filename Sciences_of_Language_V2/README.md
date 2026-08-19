# Kurdish-TSL — Sciences of Language V2

V2 upgrades the project from lexicon-level structural profiles to **complete occurrence-stream reconstruction** over every committed Deep Dictionary occurrence shard.

## Evidence base

- 14 source-specific CSTLK corpora
- Deep Dictionary V1: 47,629,049 word-like occurrences in 250 Git-tracked compressed shards
- Comparative Research V1
- Sciences of Language V1

## V2 research objects

1. complete source-local sequence statistics;
2. recurring bigrams, trigrams, four-token sequences, and longer-frame candidates;
3. discontinuous relations with explicit gap size;
4. variable-slot frames such as `A + X + B`;
5. full positional distributions rather than top-neighbor truncation;
6. complete immediate-context evidence for V1 morphology candidates;
7. competing form-family/context models;
8. cross-source construction recurrence and source-distribution entropy;
9. source/register divergence;
10. Language Graph V2 with construction/frame nodes and contradiction/risk fields.

## Epistemic rule

V2 does not start from inherited Kurdish grammatical categories. `noun`, `verb`, `subject`, `object`, `case`, `tense`, `aspect`, `suffix`, `prefix`, `ergativity`, etc. are not discovery labels.

The first layer records exact forms, exact sequences, positions, gaps, fillers, recurrence, source incidence, and counterevidence. Conventional terminology may only be proposed later as an explicitly derived interpretation.

## Two streams

V2 scans **all 47,629,049 occurrences** for coverage accounting. It separately constructs an active structural-candidate stream that requires letter-bearing/no-numeric tokens and applies documented technical/template-risk flags. Excluded material is counted and preserved; it is never deleted from the source dictionaries.

## Score rule

All V2 scores are evidence-ranking measures, **not probabilities of grammatical truth**.

## Output policy

Every retained construction has a declared retention threshold, source counts, support counts, and reproducible source-local evidence. Per-corpus intermediate packages are built independently and aggregated only after all fourteen pass their manifests.

## Full per-source pattern evidence in GitHub

All complete source-local V2 recurrent-pattern tables are repository-resident under
`Per_Source/<CORPUS>/Patterns/`. This includes all six pattern families for all fourteen
sources: BIGRAMS, TRIGRAMS, FOURGRAMS, SLOT_FRAMES, GAP2, and GAP3.

- Complete tables committed: **84/84**.
- Every compressed table passed a full gzip read/integrity check before publication.
- Every table has a SHA-256 digest, compressed byte size, and exact data-row count in
  `FULL_PATTERN_REPOSITORY_MANIFEST.json` and the source-local `FULL_PATTERN_MANIFEST.json`.
- GitHub Actions artifacts are backup/build transport only; they are not required to access the full V2 evidence.
