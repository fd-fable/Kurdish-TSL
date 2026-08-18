# Kurdish-TSL Project Context

## Project identity
- Project: The Sciences of Language — Kurdish (Kurdish-TSL / TSLK)
- Human–AI collaboration marker: `FD` = Ferhad (human researcher / native-speaker contributor); `A` = AI participation.
- Repository: `fd-fable/Kurdish-TSL`

## Core research principle
The project uses first-principles linguistic discovery. Existing Kurdish grammars, dictionaries, standardized teaching rules, external Kurdish NLP, and remembered Kurdish-specific rules are inadmissible as evidence during the blind discovery stage. General linguistic reasoning may be used as an analytical tool, but language-specific claims must be traceable to the isolated primary corpus currently under study.

The objective is not to impose a grammar on Kurdish. The objective is to discover observable structures from primary evidence, preserve uncertainty, and construct grammar only at a later synthesis stage.

## Two independent research streams
### Stream A — Documentary corpus / agent work
- Each corpus is analyzed independently.
- No cross-corpus evidence may be used during first-pass discovery.
- The agent works file-by-file and bounded-unit-by-bounded-unit.
- Raw corpus, source, earlier drafts, invalidated analyses, scripts, and later revisions are preserved for audit.
- Python may perform mechanical operations (extraction, counts, concordances, arithmetic, tables, document generation) but must not decide linguistic categories, meanings, morphemes, grammatical functions, sentence constituents, word families, or rules.

### Stream B — Native-speaker / Ferhad + ChatGPT work
- Kept isolated from Stream A until a later comparison stage.
- Includes Ferhad's natural speech, native-speaker meanings, corrections, elicited examples, stories, pronunciation, and later audio/transcription work.
- Spoken/written forms are not corrected toward standardized Kurdish.
- Existing Kurdish grammar is not used as evidence.
- Ferhad's working spellings are provisional representations; the final sound/writing system is a later research output.

## Later stages
Only after independent discovery records exist should the project perform:
1. cross-file/cross-corpus comparison;
2. comparison with native-speaker evidence;
3. grammar reconstruction;
4. testing on unseen material / additional speakers;
5. external comparison with Turkish, Arabic, Persian, neighboring languages, or prior Kurdish descriptions;
6. historical/contact/standardization analysis.

Existing descriptions are neither assumed true nor assumed false during discovery; they are simply outside the evidential base.

## Corpus/file architecture
Root corpora are numbered permanently. Current corpus folders include:
- `001_MEM_U_ZIN`
- `002_ANHA`
- `003_RONAHI`
- `004_RUDAW`
- `005_PIRTUKEN_KURMANCI_KATALOG`
- `006_KURMANJI_BEGINNERS`
- `007_KOVARA_KURMANCI`
- `008_KOVARA_HAWAR`
- `009_ROJNAMA_KURDISTAN`
- `010_KOVARA_JIN`
- `011_FOLKLORA_KURMANCA_1936`
- `012_KURD_TEAVUN_TERAKKI_1908`
- `013_ROJI_KURD_1913`
- `014_DIROK_U_CIVAKA_KURDAN`

Each source folder preserves original source material under `Sources/`, corpus documents (`CSTLK...`), linguistic diagnosis reports (`LDRSTLK...`), and later studies. A corpus can receive many separate studies; the corpus number remains stable.

Naming components in use:
- `C` = Corpora
- `LDR` = Linguistic Diagnosis Reports
- `TSL` = The Sciences of Language
- `K` = Kurdish
- sequential corpus number = `001`, `002`, etc.
- source/file name
- date (MMDDYYYY)
- `FD` = Ferhad
- `A` = AI

Examples already in repository:
- `CSTLK001MEMUZIN08172026FDA.docx`
- `LDRSTLK001MEMUZIN08172026FDA.docx`

The archive is cumulative. Do not overwrite or delete previous methodological states solely because a later analysis differs; instead label status (e.g. invalidated method test, superseded draft, active study, validated protocol version).

## Discovery methodology (current direction)
A strict two-layer architecture is required.

### Layer A — Blind Discovery Record
Observation only:
- exact forms and grapheme strings;
- counts and locators;
- distribution;
- recurring sequences;
- positional tendencies;
- neutral classes (`D...` etc.);
- structural contrasts;
- mathematical descriptions of directly observable distributions.

No conventional grammatical labels or remembered English lexical meanings may be introduced in Layer A. Orthographic symbols are not assumed to have Turkish/English/standard Kurdish sound values. Written corpora do not establish exact phonetics.

### Layer B — Interpretive Hypotheses
Only after Layer A is complete:
- propose interpretations;
- cite Layer A evidence;
- list competing hypotheses;
- list counterexamples;
- specify evidence needed to discriminate among hypotheses;
- preserve unresolved cases.

Interpretive terminology is permitted only as a hypothesis, never as inherited evidence.

## Mathematical/formal modeling requirements
Formalization follows discovery: `Data -> Observation -> Pattern -> Hypothesis -> Test -> Formal Model`.
Never begin from a formula and search for fitting examples.

Every fit metric must be fully auditable: define relevant units, support, non-conforming cases, ambiguous cases, exclusions, numerator, denominator, and complete item IDs. Avoid circular models where a class is defined by the same variable later used to validate that class.

## Current methodological history
- An initial rapid Stage 4 generated structural reports across all corpora with scripts and conventional Kurdish grammatical labels. This run was judged methodologically contaminated and must remain preserved only as an invalidated methodological test, not research evidence.
- A reset introduced bounded-unit analysis and then a two-layer discovery architecture.
- Corpus 001 Unit 1 became the pilot used to debug the research instrument.
- Important corrections included removing inherited lexical glosses, removing premature labels such as SOV/ergativity/aspect, auditing graphemic contrasts, exposing model denominators, and prohibiting circular classification.
- The intended next state is a frozen protocol (`TSLK_DISCOVERY_PROTOCOL_V1`) applied independently to bounded units across all corpora, while preserving all previous files.

## Current agent-reported milestone (requires verification against repository state)
The external agent reports having created locally:
- `TSLK_DISCOVERY_PROTOCOL_V1.docx`
- `TSLK_DISCOVERY_PROTOCOL_V1.md`
- `TSLK_METHODOLOGICAL_REPLICATION_AUDIT_V1.docx`
- `TSLK_METHODOLOGICAL_REPLICATION_AUDIT_V1.md`
- `DSRSLK001MEMUZIN08172026FDA_UNIT1_V1.docx`
- bounded Unit 1 DSR outputs for corpora 002–014
- scripts for extraction, report generation, protocol construction, and replication.

The agent reports Protocol V1 validation and a first bounded replication round across all 14 corpora. These claims must be audited before full-corpus expansion; local file creation alone is not proof that the work is methodologically valid or committed to GitHub.

## Critical audit warning for the latest replication report
Do not automatically accept high fit percentages or claims of independent replication. Before scaling full-corpus expansion, verify at least:
- the same target form set/model was not inappropriately transferred between corpora;
- each corpus's form sets/classes were independently induced;
- article/lesson/entry boundaries are genuine and not arbitrary script slices;
- all counted units and classifications are inspectable;
- Layer A contains no hidden grammatical labels;
- Layer B does not silently reuse pretrained Kurdish grammar;
- scripts did not make linguistic decisions;
- protocol validation is procedural, not validation of any Kurdish grammatical hypothesis.

## Native-speaker evidence already established in Stream B
Examples supplied by Ferhad include working forms such as:
- `Ez ke hereme male.` — speaker-supplied meaning: “I will go home.”
- `Az ke hrma mola ha.` — similar future proposition with `ha` adding an addressee-directed warning/insistence/stay/wait effect according to speaker explanation.
- `Az çûma mol.` — speaker-supplied meaning: “I went home.”
- `Ez ji mektebê hatim.` — speaker-supplied example previously discussed.

Important correction: `mol / mola / male` in Ferhad's usage refers to HOME in the relevant examples; do not infer meanings from familiar standardized Kurdish forms. Translation supplied by the speaker is semantic evidence, but internal segmentation/grammar must still be independently discovered.

Ferhad also emphasized that special letters/sounds must not inherit values from Turkish/Arabic/English visual analogies. The alphabet is a later research output, not an unquestioned input.

## Researcher background relevant to later interpretation
Ferhad has formal education in Turkish Language and Literature and extensive schooling in Arabic, plus Kurdish and some English knowledge. This multilingual knowledge may generate useful later comparative hypotheses, but it must not determine blind discovery. Comparisons supplied by Ferhad should be recorded as researcher observations, not corpus facts.

## Immediate project-management rule
When a new project chat starts, read this file and inspect the repository before asking Ferhad to repeat project history. Use the repository as the durable project-state record. Do not merge Stream B native-speaker conclusions into Stream A until explicitly authorized for the later comparative stage.
