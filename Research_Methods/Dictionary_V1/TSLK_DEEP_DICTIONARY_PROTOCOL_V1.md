# Kurdish-TSL — Deep Dictionary Protocol V1

## Status
**ACTIVE METHOD — CORPUS-SPECIFIC EXHAUSTIVE LEXICAL INVENTORY**

This protocol governs construction of deep dictionaries for every numbered Kurdish-TSL corpus.

The dictionary stage does **not** merge corpora and does **not** import external Kurdish dictionaries, grammars, translations, NLP analyses, or remembered Kurdish-specific rules as evidence.

Each corpus receives its own dictionary and its own evidence record.

---

## 1. Objective

For every corpus, construct an exhaustive lexical evidence system that:

1. does not silently discard any written vocabulary;
2. preserves every attested surface form exactly as written;
3. preserves every rare, historical, inconsistent, suspected OCR, editorial, or one-off form;
4. records frequency, position, source part, and recoverable context;
5. distinguishes exact written forms from mechanically derived search keys;
6. separates observation from interpretation;
7. leaves meaning unresolved unless later evidence establishes it;
8. is reproducible from the committed CSTLK document;
9. preserves corpus isolation;
10. can later support human/AI lexical, grammatical, semantic, historical, and spoken-language research without rewriting the primary evidence.

---

## 2. Two exhaustive token layers

### Layer R — Raw written-token inventory

The raw inventory uses whitespace-delimited strings exactly as encountered in extracted document text.

It preserves punctuation attachment and unusual written forms.

Examples of distinct raw tokens may therefore include forms such as:

- `form`
- `form,`
- `«form»`
- `form.`

Layer R exists as a completeness/audit layer. It is not a claim about linguistic word boundaries.

### Layer W — Mechanical word-like form inventory

A second inventory groups consecutive Unicode letter/mark/number characters, allowing an apostrophe or hyphen-like connector only when it occurs internally between word-like characters.

This produces searchable written-form entries.

Layer W is a **technical segmentation only**. It must not be interpreted as proof of linguistic word, morpheme, clitic, affix, or compound boundaries.

Every Layer W entry preserves its exact surface spelling.

---

## 3. No normalization of evidence

The source surface form is immutable.

Permitted derived fields include:

- Unicode NFC search key;
- Unicode casefold search key;
- character length;
- first/last character sequences;
- document-part labels;
- frequency and positional counts.

Derived keys are for search/indexing only. They must never replace the original form.

Forms differing only by capitalization, diacritic, apostrophe, historical spelling, or typographical variation remain separate surface entries.

---

## 4. Every dictionary entry

Each Layer W dictionary entry must include at least:

- Corpus ID;
- deterministic Entry ID;
- exact Surface Form;
- technical NFC key;
- technical casefold key;
- total frequency;
- number of source-document parts in which it occurs;
- first locator;
- last locator;
- sample locators;
- first attested context;
- container-initial count;
- container-final count;
- top immediately preceding forms;
- top immediately following forms;
- Unicode character length;
- exact grapheme/character sequence;
- first character;
- last character;
- first two characters where available;
- last two characters where available;
- capitalization/casefold surface relatives, when present;
- Semantic Status;
- Interpretive Status;
- Editorial/Corpus-Scope Status;
- notes field.

Default research statuses are:

`SEMANTIC VALUE UNRESOLVED`

`INTERPRETATION UNREVIEWED`

`CORPUS-SCOPE UNREVIEWED`

These defaults prevent the mechanical build from pretending to know meaning, grammatical class, or whether a token belongs to primary corpus text versus document scaffolding.

---

## 5. Occurrence evidence

The build must preserve recoverable occurrence evidence.

Every occurrence must have a stable locator based on the committed Word document structure, including where applicable:

- document part;
- paragraph number;
- table number;
- row number;
- cell number;
- paragraph-within-cell number;
- token index within the extracted container.

The dictionary summary may show only a bounded number of sample locators for readability, but the mechanical build must be capable of generating a complete occurrence/concordance stream.

---

## 6. Document scope

The extractor inventories text from the committed CSTLK Word package rather than assuming that all Word text is primary linguistic evidence.

Text is labeled by document part where recoverable, such as:

- BODY;
- HEADER;
- FOOTER;
- FOOTNOTE;
- ENDNOTE;
- other Word XML text-bearing parts.

No text is silently deleted merely because it appears editorial or metadata-like.

Later research may mark entries/occurrences as editorial scaffolding, source text, uncertain scope, etc., but that decision is separate from extraction.

---

## 7. Mechanical versus interpretive operations

### Mechanical automation MAY

- open DOCX ZIP/XML structures;
- extract text;
- assign structural locators;
- tokenize mechanically under the explicit rules above;
- count forms;
- count characters;
- calculate positional frequencies;
- calculate immediate left/right distributions;
- create technical normalization/search keys;
- group exact surface spellings by technical casefold key;
- generate TSV/JSON/Markdown files;
- compute SHA-256 hashes;
- verify coverage and determinism.

### Mechanical automation MUST NOT

- translate vocabulary;
- assign dictionary meanings;
- label nouns, verbs, adjectives, pronouns, cases, tenses, aspects, etc.;
- decide morpheme boundaries;
- decide prefixes/suffixes/clitics;
- merge surface forms into a lemma;
- declare two forms semantically equivalent;
- repair spelling;
- normalize to standard Kurdish;
- remove suspected errors;
- infer etymology;
- transfer analysis from another corpus.

---

## 8. Deep-dictionary research layers

The generated dictionary is the **lexical evidence foundation**, not the final interpreted dictionary.

Later entry enrichment may add separately versioned fields for:

### A. Distributional evidence

- recurring frames;
- positional behavior;
- co-occurrence structure;
- construction participation;
- contrast sets;
- candidate form relationships.

### B. Interpretive hypotheses

- possible semantic value;
- possible grammatical behavior;
- possible morphological relationships;
- competing analyses;
- counterexamples;
- confidence/status;
- decisive evidence needed.

### C. Native-speaker evidence

Only in Stream B or a later authorized convergence phase:

- speaker-supplied meaning;
- pronunciation/audio locator;
- pragmatic use;
- acceptability;
- elicited contrasts.

Stream B must not silently backfill Stream A.

---

## 9. Corpus isolation

Every numbered corpus has its own dictionary directory.

A form found in Corpus 001 and the visually identical form found in Corpus 002 are independent evidence records during this stage.

Do not copy meaning, grammatical category, family membership, or interpretation between them.

A project-level index may compare only mechanical metadata such as dictionary file existence and entry counts until cross-corpus comparison is explicitly authorized.

---

## 10. Completeness standard

A corpus dictionary is mechanically complete only when all of the following pass:

1. every non-empty extracted text container was processed;
2. every non-whitespace character is accounted for by the tokenizer audit;
3. every Layer W occurrence maps to exactly one dictionary surface entry;
4. sum of Layer W entry frequencies equals total Layer W occurrences;
5. sum of Layer R entry frequencies equals total raw whitespace tokens;
6. source CSTLK SHA-256 is recorded;
7. build script version/hash is recorded;
8. no source form was modified to create the Surface Form field;
9. build can be rerun deterministically from the same committed CSTLK input.

If any check fails, dictionary status must be `INCOMPLETE / AUDIT FAILED`.

---

## 11. Output package per corpus

Each corpus dictionary directory should contain:

- `README.md` — scope, source, build status, counts, methodology;
- `LEXICON.tsv` — exhaustive unique Layer W surface-form dictionary;
- `LEXICON.jsonl` — machine-readable equivalent;
- `RAW_TOKEN_INVENTORY.tsv` — exhaustive unique Layer R raw-token inventory;
- `CHARACTER_INVENTORY.tsv` — exact character inventory and counts;
- `OCCURRENCES_*.tsv` — complete Layer W occurrence/concordance shards when generated;
- `MANIFEST.json` — source hash, script hash/version, statistics, coverage checks;
- later versioned interpretive/enrichment files, never overwriting the raw lexical evidence.

Large occurrence data may be sharded to keep repository files manageable.

---

## 12. Naming

Project root:

`Dictionaries/`

Per-corpus directory:

`Dictionaries/<CORPUS_FOLDER>/`

Entry IDs are corpus-local and deterministic:

`W000001`, `W000002`, ...

Raw-token IDs:

`R000001`, `R000002`, ...

No global lemma number is assigned during isolated discovery.

---

## 13. Scientific status

A mechanically generated entry means only:

> This exact written form is attested in this committed corpus representation under the documented extraction/tokenization rules.

It does **not** by itself establish:

- pronunciation;
- meaning;
- lemma identity;
- grammatical category;
- morphological segmentation;
- historical origin;
- equivalence to a form in another corpus.

Those are later research questions.

---

## 14. Preservation

Dictionary builds are cumulative and versioned.

Do not delete rare forms, anomalies, historical forms, or suspected extraction artifacts. Flag them later if evidence warrants.

The guiding principle is:

> **Preserve first. Index exhaustively. Interpret separately. Never make missing evidence look like clean language.**
