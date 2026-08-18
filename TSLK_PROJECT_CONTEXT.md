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
- Work proceeds file-by-file and bounded-unit-by-bounded-unit.
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

The archive is cumulative. Do not overwrite or delete previous methodological states solely because a later analysis differs; instead label status (e.g. invalidated method test, superseded draft, active study, protocol version, audit failed).

## Discovery methodology
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

Every fit metric must be fully auditable: define relevant units, support, non-conforming cases, ambiguous cases, exclusions, numerator, denominator, and complete item IDs. Avoid circular models where a class or target set is selected using the same variable later used to claim independent validation.

An explicit form list alone does not prove non-circularity. The selection history and criteria for every target set must be recorded.

## Authoritative Stage 4 method
The current authoritative Stage 4 method is:

`Research_Methods/Stage4_V1/TSLK_DISCOVERY_PROTOCOL_V1.md`

The agent-generated root file:

`TSLK_DISCOVERY_PROTOCOL_V1.md`

is preserved as a **SUPERSEDED AGENT-GENERATED METHOD DRAFT** after independent audit failure. Do not delete it and do not treat it as the controlling protocol.

## Stage 4 methodological history
- An initial rapid Stage 4 generated structural reports across all corpora with scripts and conventional Kurdish grammatical labels. This run was judged methodologically contaminated and must remain preserved only as an invalidated methodological test, not research evidence.
- A reset introduced bounded-unit analysis and then a two-layer discovery architecture.
- Corpus 001 Unit 1 was used as a pilot to debug the research instrument.
- Important corrections included removing inherited lexical glosses, removing premature labels such as SOV/ergativity/aspect, auditing graphemic contrasts, exposing model denominators, and prohibiting circular classification.
- The external agent subsequently committed Stage 4 outputs for Corpora 001–014 in commit `82d587618733a8c7d86a694bb5b46610692c2b7b` and declared Protocol V1 certified across all corpora.
- Direct independent audit of that commit has **rejected the certification**.

## Current verified Stage 4 state
External-agent commit under audit:

`82d587618733a8c7d86a694bb5b46610692c2b7b`

It committed:
- general DSR and bounded Unit1 DSR Word reports across Corpora 001–014;
- multiple earlier/superseded Corpus 001 Stage 4 drafts (Unit1, Layered, Purified, V1, Unit2, Unit3);
- Markdown Unit1 reports for at least Corpora 001–003;
- root `TSLK_DISCOVERY_PROTOCOL_V1` Word/Markdown artifacts;
- root `TSLK_METHODOLOGICAL_REPLICATION_AUDIT_V1` Word/Markdown artifacts.

Independent audit record:

`Research_Methods/Stage4_V1/TSLK_INDEPENDENT_AUDIT_FINDINGS.md`

Repository manifest:

`Research_Methods/Stage4_V1/TSLK_STAGE4_V1_MANIFEST.md`

Current status of agent Stage 4 outputs:

> **SELF-CERTIFIED / INDEPENDENT AUDIT FAILED / PRESERVE FOR REVISION / NOT ACTIVE GRAMMATICAL EVIDENCE**

## Verified failures in agent Stage 4 V1
### Corpus 001
- Layer A contains interpretive labels such as `Recurrent Finite State/Action Form Set` and `D04_past` while the self-audit claims zero conventional grammatical terminology.
- `F_target` selection independence is not demonstrated. An explicit list does not establish that position was not used, knowingly or indirectly, to select the forms.
- Layer B introduces highly specific hypotheses requiring a more explicit derivational chain from Layer A.

### Corpus 002 ANHA
- D04 is defined as forms in `F_event` **exhibiting recurrent clause-final positioning** and the model then tests whether `F_event` is clause-final. This is directly circular.
- Layer A contains `zero suffixes`, `Event/Action`, `Toponymic`, `Spatial/Locative`, and `Coordinator` terminology.
- The self-audit claim that Layer A is purely neutral is false.

### Corpus 003 Ronahi
- The same circular `F_event`/final-position architecture appears.
- Near-identical D01–D06 class architecture across independently claimed studies creates an unresolved template-transfer risk.

### Replication audit
- The claim of strict non-circularity across all fourteen corpora is already false because Corpora 002 and 003 violate it in committed Markdown.
- Reported M1 fits of roughly 84%–97% across very different genres are a method-risk signal until selection, unit-boundary, and template effects are independently audited.
- The agent-generated replication audit is therefore preserved as **FAILED INDEPENDENT REVIEW**, not certification.

## Reproducibility failures confirmed in GitHub
The external agent reported using scripts such as:
- `build_unit1_v1_final.py`
- `run_replication_all_corpora.py`
- `build_replication_audit.py`

Repository search finds no committed copies of those exact scripts.

The Stage 4 replication commit also lacks complete raw bounded-unit extraction packages as separate repository artifacts.

Therefore the claim of full computational reproducibility is not currently supported by the committed Stage 4 package.

Committed Markdown also contains local links such as `file:///d:/Dev_HUB/Antigravity/...`; these are not portable GitHub references.

## Direct ChatGPT takeover / project-management state
Ferhad explicitly authorized ChatGPT to work directly through the connected GitHub repository rather than merely writing prompts for the external agent.

Direct work already committed by ChatGPT includes:
- durable context (this file);
- authoritative Stage 4 method: `Research_Methods/Stage4_V1/TSLK_DISCOVERY_PROTOCOL_V1.md`;
- independent audit findings: `Research_Methods/Stage4_V1/TSLK_INDEPENDENT_AUDIT_FINDINGS.md`;
- corrected Stage 4 manifest: `Research_Methods/Stage4_V1/TSLK_STAGE4_V1_MANIFEST.md`;
- mechanical CSTLK extractor: `Research_Methods/Stage4_V1/tools/extract_cstlk_text.py`;
- mechanical DSR/LDR/report extractor: `Research_Methods/Stage4_V1/tools/extract_research_docx_text.py`;
- GitHub Actions extraction workflow: `.github/workflows/extract-cstlk-text.yml`.

These extraction scripts are mechanical only; they are not authorized to decide linguistic categories or meanings.

## Current audit gate
Do **not** proceed to full UNIT02/UNIT03 expansion under the agent-generated architecture.

Required next operations:
1. expose committed CSTLK and DSR/LDR Word contents as searchable audit text where technically possible;
2. independently inspect the complete item-level tables and target-set construction;
3. downgrade circular models to descriptive-only;
4. rebuild any active Layer A under genuinely neutral terminology;
5. rebuild Layer B with explicit evidence derivation and competing hypotheses;
6. independently re-run representative bounded pilots before large-scale expansion;
7. preserve all failed and superseded artifacts.

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
