# TSLK Discovery Protocol V1

## Status
**AUTHORITATIVE METHOD VERSION: V1**

Project: The Sciences of Language - Kurdish (Kurdish-TSL / TSLK)

Human-AI research attribution: `FD` = Ferhad; `A` = AI participation.

This protocol governs Stage 4 documentary-corpus discovery. It does **not** validate any Kurdish grammatical hypothesis. It defines how evidence must be collected, separated from interpretation, tested, formalized, audited, and preserved.

---

## 1. Central research mandate

The project must not apply a known grammar to the corpus. It must discover possible linguistic structure from the primary evidence itself.

Required order:

`PRIMARY DATA -> OBSERVATION -> DISTRIBUTION -> CONTRAST -> HYPOTHESIS -> PREDICTION -> COUNTEREXAMPLE SEARCH -> TEST -> REVISION -> FORMALIZATION -> PROVISIONAL STATUS`

Never reverse this order by starting from a known Kurdish rule, conventional grammar category, dictionary meaning, mathematical formula, or cross-corpus pattern and searching for matching examples.

Existing Kurdish descriptions are neither accepted nor rejected during blind discovery. They are outside the evidential base.

---

## 2. Absolute corpus isolation

Each numbered corpus is an independent experiment during first-pass discovery.

While Corpus `00X` is active:

- do not use another corpus to explain it;
- do not transfer form classes, meanings, paradigms, sentence structures, or rules from another corpus;
- do not use another author/source to fill missing evidence;
- do not use the native-speaker research stream;
- do not use prior Kurdish grammars, dictionaries, teaching materials, online explanations, translation systems, Kurdish NLP analyzers, or remembered Kurdish-specific rules as evidence.

The same-looking form appearing in two corpora must be independently rediscovered in each corpus.

Cross-corpus comparison is a later phase and must be explicitly authorized.

---

## 3. Evidence hierarchy

Evidence must be classified by source and epistemic status.

### E0 - Primary source
Original PDF, scan, book, newspaper, periodical, or other source material stored under `Sources/`.

### E1 - Corpus representation
The corresponding `CSTLK...` corpus document. It is a research representation of the source and must not silently overwrite source variation.

### E2 - Layer A observation
Directly observable facts from one isolated bounded unit.

### E3 - Layer B hypothesis
Interpretation proposed only after Layer A exists.

### E4 - Candidate rule
A hypothesis that has survived repeated internal testing and counterexample search within the same corpus. This remains corpus-specific.

### E5 - Later comparative result
Cross-unit/cross-corpus/native-speaker comparison. Not permitted during the current independent first-pass stage.

No claim may be promoted by skipping an evidence level.

---

## 4. Preserve the archive

Never delete or overwrite earlier methodological states merely because later work improves them.

Preserve:

- primary sources;
- CSTLK corpora;
- LDR reports;
- invalidated Stage 4 experiments;
- superseded drafts;
- raw bounded-unit extractions;
- scripts;
- audit tables;
- calculations;
- protocol versions;
- active DSR studies.

Use explicit status labels such as:

- `PRIMARY SOURCE`
- `CORPUS`
- `PRELIMINARY REPORT`
- `INVALIDATED METHOD TEST`
- `SUPERSEDED DRAFT`
- `PILOT`
- `ACTIVE DISCOVERY STUDY`
- `METHOD VERSION`
- `AUDIT PENDING`

Invalidated means excluded from the evidential chain, not erased from history.

---

## 5. Bounded-unit principle

Do not analyze an entire large corpus in one linguistic pass.

Divide each corpus into natural bounded units appropriate to its source type.

Examples:

- poetry: a defined run of lines/couplets/sections;
- newspaper/news agency: complete article(s), never arbitrary sentence slices presented as complete articles;
- periodical: complete article or coherent section;
- book/prose: chapter subsection or coherent passage;
- pedagogical material: lesson/dialogue boundaries;
- catalog: complete entries;
- folklore: complete episode or coherent narrative segment.

For every bounded unit record:

1. corpus ID;
2. source file;
3. exact start locator;
4. exact end locator;
5. unit-selection rule;
6. why the boundary is natural;
7. whether the unit is complete or partial.

Do not select units because they conveniently support a hypothesis.

---

## 6. Two-layer architecture

### Layer A - Blind Discovery Record

Layer A contains observation only.

Permitted:

- exact grapheme strings;
- token strings;
- exact locators;
- counts;
- position;
- adjacency;
- recurrence;
- co-occurrence;
- surface variation;
- repeated sequences;
- distributional frames;
- neutral form sets;
- neutral structural classes;
- graphemic contrasts;
- quantitative descriptions of observable distributions;
- contradictions and ambiguous cases.

Not permitted in Layer A unless independently established as an observable convention of the file:

- noun;
- verb;
- adjective;
- pronoun;
- subject;
- object;
- predicate;
- agent;
- patient;
- case;
- gender;
- number;
- tense;
- aspect;
- mood;
- ergative;
- nominative;
- oblique;
- prefix;
- suffix;
- clitic;
- adposition;
- linker;
- head;
- modifier;
- SOV/SVO/VSO;
- remembered English lexical glosses.

If exact meaning is not internally demonstrable, write:

`SEMANTIC VALUE UNRESOLVED`

If structural status is not demonstrable, write:

`STRUCTURAL STATUS UNRESOLVED`

### Layer B - Interpretive Hypotheses

Only after Layer A for the phenomenon is complete may Layer B propose interpretations.

Every Layer B hypothesis must contain:

1. hypothesis ID;
2. precise proposal;
3. Layer A evidence IDs;
4. supporting examples;
5. contradictory examples;
6. at least one competing hypothesis when plausible;
7. prediction that would distinguish the hypotheses;
8. current confidence/status;
9. evidence still required.

Conventional linguistic terminology may appear only as a hypothesis label, not as inherited evidence.

---

## 7. Neutral identifier system

Use stable identifiers within each corpus/unit.

Suggested prefixes:

- `G###` - grapheme/graphemic observation;
- `GC###` - graphemic contrast;
- `F###` - exact observed form;
- `S###` - segment candidate with unresolved status;
- `D###` - distributional class;
- `P###` - positional pattern;
- `CO###` - co-occurrence pattern;
- `SF###` - structural/sentence-form template;
- `H###` - hypothesis;
- `M###` - formal/mathematical model;
- `EX###` - exception/non-conforming observation;
- `AMB###` - ambiguous observation;
- `Q###` - open question;
- `REV###` - revision event.

IDs must remain stable when a hypothesis is revised. Do not reuse an ID for a different claim.

---

## 8. Graphemic and orthographic discovery

Treat written characters as observed symbols, not automatic phonetic facts.

Do not inherit sound values from Turkish, English, Arabic transliteration, standard Kurdish, or any other language merely because the same visual symbol is used.

Layer A may study:

- grapheme inventory;
- case distinctions in writing;
- diacritics;
- grapheme frequencies;
- recurrent sequences;
- word-internal positions;
- punctuation;
- capitalization;
- spelling variants;
- single-property graphemic contrasts.

A minimal graphemic contrast must differ in exactly one defined graphemic property under the comparison criterion. If more than one property differs, label it a near contrast/general comparison.

Written corpora alone do not establish exact pronunciation, phonemes, stress, vowel quality, consonant realization, or intonation. Record such matters as requiring later spoken evidence.

---

## 9. Word and form-development discovery

The objective is to discover repeated form relationships without assuming conventional morphology.

For recurring forms:

1. record each exact surface form;
2. collect every occurrence in the bounded unit;
3. identify shared and variable grapheme material;
4. map positions of the variable material;
5. compare contexts;
6. search for apparently related forms;
7. test whether similarity is systematic or accidental;
8. preserve unattested combinations as `UNATTESTED` rather than filling paradigms.

A proposed form-family network must distinguish:

- directly observed similarity;
- proposed segmentation;
- proposed relationship;
- unresolved alternatives.

Do not call a segment a root, prefix, suffix, ending, clitic, derivation, inflection, or compound in Layer A. Such labels belong in Layer B if earned by evidence.

---

## 10. Distributional-class discovery

A distributional class must be defined by observable frames.

Example neutral definition:

`D003 = forms occurring in frame X __ Y in at least N independently cited observations and also occurring in frame Z __ in at least M observations.`

Do not define a class by a grammatical label.

Record:

- inclusion criteria;
- members;
- excluded candidates;
- borderline candidates;
- frequency;
- frames;
- counterexamples.

A class definition must not contain the same variable later used as statistical proof of that class unless the analysis explicitly treats the result as descriptive rather than confirmatory.

---

## 11. Sentence/structure discovery

Do not assume subject/object/verb or a standard word order.

For each informative unit:

1. preserve the exact original text;
2. assign a stable locator;
3. identify recurrent strings/classes;
4. record positions;
5. compare structurally similar examples;
6. note additions/deletions/substitutions/reordering;
7. propose neutral templates;
8. search for structures that fail the template.

Early templates use neutral labels:

`SF001 = D001 + D004 + F017`

not:

`S + O + V`

until those conventional categories have themselves been independently argued.

---

## 12. Contrast and substitution analysis

Search for examples differing in one or a small number of observable properties.

Record:

- exact forms/sentences;
- what is held constant;
- what changes;
- whether the contrast is graphemic, positional, distributional, or contextual;
- whether semantics are independently recoverable.

Do not call a pair semantically minimal if the semantic difference comes only from remembered Kurdish knowledge.

---

## 13. Co-occurrence and dependency discovery

For forms/classes X and Y measure where useful:

- count(X);
- count(Y);
- count(X,Y);
- order;
- distance;
- boundary position;
- conditional frequency.

Possible notation:

`P(Y | X, E)`

where `E` is a precisely defined observable environment.

Co-occurrence is not automatically dependency, morphology, syntax, or meaning. Those are Layer B hypotheses.

---

## 14. Formal and mathematical modeling

Mathematics describes discovered evidence; it does not generate linguistic truth.

Permitted representations include:

- sets: `C = {x1, x2, ...}`;
- sequences: `S = [x1, x2, ... xn]`;
- conditional frequency: `P(Y | X,E)`;
- observable alternation: `A ~ B / E`;
- structural template: `SF = X1 + X2 + X3`;
- graph: `G = (V,E)` where every edge is evidence-backed;
- fit calculation where relevance/support rules are defined independently.

Required order:

`Observation -> Pattern -> Hypothesis -> Test definition -> Formal model`

Never:

`Formal model -> search for favorable examples`

---

## 15. Anti-circularity rule

A model is circular if the tested property was also materially used to select or define the tested class/set.

Before every fit metric, answer:

1. How was the target set/class created?
2. Was the tested variable known during selection?
3. Were candidates rejected based on the tested outcome?
4. Is the selection criterion independent of the tested variable?

If independence cannot be demonstrated, classify the result as:

`DESCRIPTIVE ONLY - NOT AN INDEPENDENT TEST`

Do not call it validation.

---

## 16. Fit metrics and reproducibility

Every percentage must expose the full denominator.

For every model include:

- Model ID;
- model definition;
- target population;
- relevant-unit rule;
- support rule;
- non-conforming rule;
- ambiguity rule;
- exclusion rule;
- complete unit IDs;
- numerator;
- denominator;
- exact calculation.

Recommended audit table:

| Unit ID | Raw evidence locator | Target present? | Observable value | Classification | Reason |
|---|---|---|---|---|---|

No hidden exclusions.

A high percentage is not itself a grammatical rule. Investigate whether it can arise from genre, source formatting, punctuation, extraction method, sampling, unit boundary definition, target-set selection, or other artifacts.

---

## 17. Exceptions and counterexamples

Do not delete outliers to improve model fit.

Create an exception register:

| ID | Locator | Expected observable pattern | Observed pattern | Current explanations | Status |
|---|---|---|---|---|---|

A single well-supported counterexample may require narrowing or rejecting a hypothesis.

---

## 18. Competing hypotheses

When evidence admits multiple explanations, preserve them.

Example neutral architecture:

- `H001a`: X and Y are parts of one larger structural unit.
- `H001b`: X and Y are independent adjacent units.
- `H001c`: apparent relationship results from orthographic convention.

Specify what future evidence would distinguish the models.

Do not ask the researcher to choose among ordinary analytical alternatives; preserve unresolved competition.

---

## 19. Semantics

Semantic discovery is permitted only when supported internally by the isolated corpus.

For a candidate semantic interpretation:

- collect all occurrences;
- identify contexts shared across occurrences;
- identify contexts that differ;
- distinguish textual inference from remembered lexical knowledge;
- state uncertainty.

If the bounded unit does not independently establish the value, use:

`SEMANTIC VALUE UNRESOLVED`

Do not use external dictionaries or automatic translation to resolve it during blind discovery.

---

## 20. Spoken-evidence boundary

Questions that require sound must be recorded rather than guessed.

Examples:

- stress;
- intonation;
- vowel duration;
- phoneme contrast;
- consonant realization;
- acoustic boundary evidence;
- whether two written forms are pronounced identically.

Mark:

`REQUIRES LATER SPOKEN EVIDENCE`

Do not import Stream B native-speaker evidence into Stream A during independent discovery.

---

## 21. Mechanical tools vs linguistic judgment

Python/scripts may perform mechanical operations, including:

- extraction;
- character/token counts;
- locating strings;
- concordance creation;
- position calculations;
- arithmetic;
- table generation;
- document generation;
- hashing/version checks.

Scripts must not autonomously decide:

- linguistic categories;
- lexical meanings;
- word families;
- morphemes;
- grammatical functions;
- sentence constituents;
- semantic equivalence;
- grammatical rules;
- which counterexamples are linguistically irrelevant.

Every linguistic judgment must be made after direct AI inspection of the cited primary examples and must be recorded as judgment rather than mechanical fact.

Recommended provenance markers:

- `M` = mechanical result;
- `J` = AI linguistic judgment;
- `S` = source fact;
- `H` = hypothesis.

---

## 22. Mandatory self-audit

Every bounded study must pass these audits before it is marked complete.

### A. Observation-purity audit
Could each Layer A statement be written solely from the isolated bounded text without Kurdish-specific prior knowledge?

### B. Evidence-traceability audit
Can every claim be reconstructed from exact evidence locators?

### C. Circularity audit
Does a test use the same property both to select a class/set and to validate it?

### D. Semantic-contamination audit
Did any remembered translation or known Kurdish grammatical meaning enter as evidence?

### E. Cross-corpus contamination audit
Was another corpus used to resolve the current corpus?

### F. Mathematical-reproducibility audit
Can every numerator, denominator, exclusion, ambiguity, and classification be independently reconstructed?

### G. Counterexample audit
Was evidence against each major hypothesis actively searched?

The audit may fail. If it fails, record failure, revise the analysis, and preserve the earlier version.

---

## 23. Replication across corpora

The protocol may be standardized across corpora; findings must not be standardized.

Every corpus may yield different:

- form inventories;
- distributional classes;
- structural patterns;
- model types;
- uncertainty levels;
- amount of recoverable semantics.

Do not force all corpora into identical sections, form sets, sentence templates, or mathematical models.

During the first replication round, compare only **method performance**, not grammatical findings.

Cross-corpus linguistic synthesis is prohibited until every corpus has an independent discovery record sufficient for comparison.

---

## 24. Study output package

Every active Stage 4 bounded unit should eventually preserve:

1. raw bounded-unit evidence;
2. source locator map;
3. Layer A record;
4. Layer B hypotheses;
5. form inventory;
6. distributional-class register;
7. structural-template register;
8. formal-model definitions;
9. complete calculation/audit tables;
10. exception register;
11. competing-hypothesis register;
12. open-questions register;
13. self-audit results;
14. scripts used for mechanical work;
15. final report artifact if generated.

Each artifact must state its protocol version.

---

## 25. Version control

This file is Protocol V1.

Do not silently modify the scientific method after studies have been produced under it.

If a methodological correction is necessary:

- preserve V1;
- create V1.1/V1.2 for compatible corrections or V2 for material redesign;
- record why the change occurred;
- identify which studies were produced under each version;
- determine whether earlier studies require re-analysis.

---

## 26. Stop condition for current discovery phase

The current stage ends only after sufficient independent evidence has accumulated within each corpus to justify later comparison.

Do not construct a final Kurdish grammar during Stage 4.

The long-term sequence is:

`Independent documentary discovery -> independent native-speaker discovery -> controlled comparison -> grammar reconstruction -> held-out testing -> revision -> later external/historical/contact comparison`

---

## 27. Final operational rule

**Same protocol, independent evidence, no transferred grammar.**

For every corpus:

> Observe first.
> Preserve raw evidence.
> Keep Layer A free of inherited interpretation.
> Form hypotheses only after observations exist.
> Test hypotheses against counterexamples.
> Formalize only what has been operationally defined.
> Expose every calculation.
> Preserve uncertainty.
> Stop before final grammar construction.
