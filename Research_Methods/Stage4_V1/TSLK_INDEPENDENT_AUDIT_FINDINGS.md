# TSLK Stage 4 V1 — Independent Audit Findings

## Status
**INDEPENDENT AUDIT: FAILED AT CURRENT SELF-CERTIFIED V1 STATE**

This document records an independent methodological review of the Stage 4 materials committed in:

`82d587618733a8c7d86a694bb5b46610692c2b7b`

Commit message:

`feat(discovery): freeze Protocol V1, validate Corpus 001 Unit 1, and replicate across Corpora 002-014`

The findings below do **not** delete or erase any Stage 4 artifact. They change evidential status only.

All agent-generated DSR studies in that commit remain preserved as research-history artifacts, but they are not currently accepted as validated Stage 4 evidence.

---

## 1. Executive finding

The agent-generated root-level `TSLK_DISCOVERY_PROTOCOL_V1` and its replication reports contain methodological contradictions that invalidate their own claim of successful independent validation.

Major problems found directly in committed Markdown include:

1. Layer A contains non-neutral grammatical/semantic terminology while claiming such terminology is absent.
2. Some mathematical target sets are defined partly by the positional property subsequently tested, producing circularity.
3. Merely supplying an explicit lexical/form list is incorrectly treated as proof that set selection was independent of the tested variable.
4. Similar class architectures and model structures recur across supposedly isolated corpora, raising a template-transfer risk that requires audit.
5. Self-audit results are treated as certification rather than internal checks.
6. High model-fit values across very different genres are declared evidence of protocol success without adequate assessment of unit-selection, target-set-selection, extraction, and template effects.
7. Some Layer B hypotheses introduce highly specific linguistic terminology without documenting an internal derivational chain sufficient to distinguish corpus-based inference from pretrained Kurdish knowledge.

Therefore the current status is:

> **AGENT V1 REPLICATION — SELF-CERTIFIED / INDEPENDENT AUDIT FAILED / PRESERVE FOR REVISION**

---

## 2. Corpus 001 audit findings

Source under audit:

`001_MEM_U_ZIN/Stage_4_Discovery_Study_Corpus001_Unit1_V1.md`

### 2.1 Layer A contamination

The report states that Layer A has zero conventional grammatical terminology, but Layer A contains:

- `Recurrent Finite State/Action Form Set`
- `D04_past`

These descriptions are not purely observable graphemic/positional facts.

`Finite`, `State`, `Action`, and `past` introduce grammatical/semantic interpretation.

### 2.2 D04 form-set independence is not demonstrated

The report states:

`Class D04 = forms listed in F_target that exhibit recurring structural co-occurrence across clauses`

and then tests final-position behavior of the same target set.

The audit claims non-circularity because D04 is an “explicit form set” and position is the tested variable.

That is insufficient.

An explicit list does not prove independent selection.

Required missing information:

- how each F_target member was selected;
- whether final-position frequency was known before selection;
- whether non-final candidates were rejected;
- whether the target list was generated from known linguistic intuitions;
- what observable criterion, independent of position, defines membership.

Until this information exists, M1 must be classified:

`SELECTION-INDEPENDENCE UNVERIFIED`

and not as a validated non-circular test.

### 2.3 Layer B evidential overreach risk

H001 proposes:

- head-initial modifier dependency;
- agreement;
- phonological clitic status as competitor.

These are permissible as hypotheses only if the report documents a sufficient Layer-A-derived evidential chain and alternative analyses. The current summary does not demonstrate that these categories were independently derived rather than imported as familiar grammatical concepts.

Status:

`INTERPRETIVE HYPOTHESIS — REQUIRES DERIVATIONAL AUDIT`

### 2.4 Self-certification failure

The report marks all six internal audit tests as passed and then certifies the pilot method as validated.

This cannot substitute for independent methodological review.

The independent review has identified false statements in the self-audit, so the self-certification is withdrawn as evidential status.

---

## 3. Corpus 002 ANHA audit findings

Source under audit:

`002_ANHA/Stage_4_Discovery_Study_Corpus002_Unit1.md`

### 3.1 Direct circularity in D04 / M1

Layer A defines D04 as:

> forms listed in `F_event` **exhibiting recurrent clause-final positioning**

The mathematical model then tests:

> whether the final token belongs to `F_event`

This is direct circularity because clause-final positioning participates in the target-set definition and is then measured as the model outcome.

M1 ANHA cannot be interpreted as an independent confirmation of clause-final preference.

Required status:

`M1-ANHA — CIRCULAR / DESCRIPTIVE ONLY`

The reported `43/50 = 86.00%` may remain as a descriptive statistic if its item classifications are correct, but it must not be presented as independent model support.

### 3.2 Layer A grammatical/semantic leakage

Layer A includes:

- `zero suffixes`
- `Recurrent Event/Action Form Set`
- `Toponymic and institutional proper strings`
- `Spatial / Locative Entity Strings`
- `Binary Invariant Coordinator`

These are not fully blind descriptive labels.

The self-audit statement that Layer A uses “pure neutral classes” is therefore false.

### 3.3 Layer B specific-language contamination risk

H-ANHA-01 introduces:

- `Periphrastic Event Reporting Pattern`
- `Action-Noun`
- `affected entity occupies pre-verbal position`
- competitor `Motion verb in serial verb construction`

H-ANHA-02 introduces:

- `Prepositional frames`
- `Toponym`
- `thematic setting frame`

These are not prohibited in Layer B, but they require explicit internal derivation from Layer A. The report currently does not expose enough derivational evidence to establish that they were independently discovered rather than supplied by pretrained Kurdish knowledge or generic templating.

Status:

`LAYER B — REQUIRES INDEPENDENT DERIVATIONAL AUDIT`

---

## 4. Corpus 003 Ronahi audit findings

Source under audit:

`003_RONAHI/Stage_4_Discovery_Study_Corpus003_Unit1.md`

### 4.1 Same circular architecture as Corpus 002

D04 is defined as forms in `F_ron_event`:

> exhibiting recurrent clause-final positioning

M1 then tests final positioning of `F_ron_event`.

Status:

`M1-RONAHI — CIRCULAR / DESCRIPTIVE ONLY`

### 4.2 Repeated class architecture risk

Corpus 002 and Corpus 003 reproduce nearly the same D01–D06 class architecture and semantic class descriptions.

Similarity across independent corpora is not itself invalid, but at this stage it creates a serious question:

> Was the class inventory independently induced in Corpus 003, or was the Corpus 002 template reused and populated with new examples?

This must be resolved by inspecting scripts, selection procedures, and raw bounded-unit evidence.

Status:

`CROSS-CORPUS TEMPLATE-TRANSFER RISK — OPEN`

---

## 5. Root Protocol V1 audit findings

Source:

`TSLK_DISCOVERY_PROTOCOL_V1.md`

The root agent-generated protocol is preserved but is no longer the authoritative methodological standard.

The authoritative independent-audit standard is:

`Research_Methods/Stage4_V1/TSLK_DISCOVERY_PROTOCOL_V1.md`

Problems in the root protocol include:

- use of `syntactic environments` while defining a supposedly blind layer;
- section heading `Morphological Sequences` for strings whose morphological status is supposed to remain unresolved;
- self-certification language;
- a narrower audit framework than the independently authored Stage 4 V1 protocol;
- no robust evidence hierarchy;
- insufficient target-set selection provenance requirements;
- insufficient distinction between descriptive frequency and independent statistical test.

Status of root protocol:

`SUPERSEDED AGENT-GENERATED METHOD DRAFT — PRESERVE, DO NOT DELETE`

---

## 6. Replication audit failure

Source:

`TSLK_METHODOLOGICAL_REPLICATION_AUDIT_V1.md`

The replication audit claims:

- universal applicability;
- strict non-circularity across all 14 corpora;
- full reproducibility;
- certification and validation across all 14.

At least the non-circularity claim is already demonstrably false for Corpora 002 and 003 from the committed Markdown itself.

Therefore the final certification statement is withdrawn from active evidential status.

Status:

`SELF-REPLICATION AUDIT — FAILED INDEPENDENT REVIEW`

---

## 7. Uniform M1 fit risk

Reported M1 values across the fourteen pilot units range approximately from 84% to 97% despite large genre differences.

This pattern must not be interpreted as grammatical convergence until the following are audited independently:

1. target-set selection rules;
2. timing of target-set creation relative to positional inspection;
3. bounded-unit selection rules;
4. sentence/headline/entry boundary definitions;
5. classification scripts;
6. exclusions and ambiguous-case handling;
7. whether common code/template logic imposed the same analysis architecture;
8. whether high fit is partly a consequence of selecting forms already recognized as event/state forms through pretrained knowledge.

Status:

`M1 CROSS-CORPUS UNIFORMITY — METHOD RISK, NOT LANGUAGE FINDING`

---

## 8. Required remediation before expansion

Do not begin full-corpus UNIT02/UNIT03 expansion under the agent-generated V1 analysis architecture.

Required sequence:

1. mechanically extract committed CSTLK and DSR Word documents into searchable text with hashes and stable locators;
2. inspect the complete item-level audit tables;
3. reconstruct target-set selection history for each corpus;
4. reclassify circular models as descriptive-only;
5. rebuild Layer A with strictly neutral terminology;
6. rebuild Layer B with explicit derivational chains from Layer A;
7. preserve all failed/superseded versions;
8. issue a protocol revision only after audit evidence requires it;
9. independently re-run a bounded pilot on at least a representative subset of corpus types before large-scale expansion.

---

## 9. Evidential statuses after this audit

| Artifact class | Current status |
|---|---|
| Sources | PRIMARY EVIDENCE |
| CSTLK corpora | CORPUS EVIDENCE, subject to source fidelity checks |
| LDRSTLK reports | PRELIMINARY ANALYSIS, not Stage 4 proof |
| Initial rapid DSR files | INVALIDATED METHOD TEST / PRESERVED |
| Agent Unit1 / V1 DSR files from commit 82d5876 | PRE-AUDIT / SELF-CERTIFIED / NOT ACTIVE EVIDENCE |
| Agent root `TSLK_DISCOVERY_PROTOCOL_V1` | SUPERSEDED METHOD DRAFT / PRESERVED |
| Agent `TSLK_METHODOLOGICAL_REPLICATION_AUDIT_V1` | FAILED INDEPENDENT REVIEW / PRESERVED |
| `Research_Methods/Stage4_V1/TSLK_DISCOVERY_PROTOCOL_V1.md` | AUTHORITATIVE CURRENT METHOD |
| This audit file | ACTIVE INDEPENDENT AUDIT RECORD |

---

## 10. Scientific principle

The failure of a self-certification does not imply that every observed pattern is false.

It means only that the current analysis does not yet establish those patterns under the project's required evidential standard.

The correct response is not deletion. It is:

`Preserve -> Audit -> Separate observation from interpretation -> Re-test -> Revise status`.
