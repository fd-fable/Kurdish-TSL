# TSLK Stage 4 V1 Repository Manifest

## Status
**STAGE 4 V1 — INDEPENDENT AUDIT FAILED / REMEDIATION IN PROGRESS**

This manifest records the actual committed GitHub state after agent commit:

`82d587618733a8c7d86a694bb5b46610692c2b7b`

Authoritative project context:

`TSLK_PROJECT_CONTEXT.md`

Authoritative current Stage 4 method:

`Research_Methods/Stage4_V1/TSLK_DISCOVERY_PROTOCOL_V1.md`

Independent audit record:

`Research_Methods/Stage4_V1/TSLK_INDEPENDENT_AUDIT_FINDINGS.md`

Agent root protocol/audit documents remain preserved, but they are not authoritative after independent audit failure.

---

## Status vocabulary

- `PRIMARY SOURCE` — original material under `Sources/`.
- `CORPUS EVIDENCE` — CSTLK representation, subject to source-fidelity checks.
- `PRELIMINARY ANALYSIS` — LDR material.
- `INVALIDATED METHOD TEST` — preserved but excluded from active evidence.
- `SELF-CERTIFIED / PRE-AUDIT` — agent Stage 4 artifact not independently accepted.
- `FAILED INDEPENDENT AUDIT` — methodological claims contradicted by direct review.
- `ACTIVE V1` — reserved for a study that passes the authoritative independent protocol.

No DSR currently has `ACTIVE V1` status.

---

## Committed corpus inventory after agent push

All numbered corpora 001–014 now contain Stage 4 DSR material from the external-agent run committed in `82d5876...`.

| ID | Corpus folder | Base CSTLK/LDR/Sources | Agent Stage 4 state | Active evidential status |
|---|---|---|---|---|
| 001 | `001_MEM_U_ZIN` | Present | general DSR; Unit1; Layered; Purified; Unit1 V1; Unit2; Unit3; Markdown Unit1 V1 | **SELF-CERTIFIED / PRE-AUDIT; key claims failed independent audit** |
| 002 | `002_ANHA` | Present | general DSR; Unit1; Markdown Unit1 | **FAILED INDEPENDENT AUDIT: circular M1 + Layer A leakage** |
| 003 | `003_RONAHI` | Present | general DSR; Unit1; Markdown Unit1 | **FAILED INDEPENDENT AUDIT: circular M1 + template-transfer risk** |
| 004 | `004_RUDAW` | Present | general DSR; Unit1 | **SELF-CERTIFIED / PRE-AUDIT** |
| 005 | `005_PIRTUKEN_KURMANCI_KATALOG` | Present | general DSR; Unit1 | **SELF-CERTIFIED / PRE-AUDIT** |
| 006 | `006_KURMANJI_BEGINNERS` | Present | general DSR; Unit1 | **SELF-CERTIFIED / PRE-AUDIT** |
| 007 | `007_KOVARA_KURMANCI` | Present | general DSR; Unit1 | **SELF-CERTIFIED / PRE-AUDIT** |
| 008 | `008_KOVARA_HAWAR` | Present | general DSR; Unit1 | **SELF-CERTIFIED / PRE-AUDIT** |
| 009 | `009_ROJNAMA_KURDISTAN` | Present | general DSR; Unit1 | **SELF-CERTIFIED / PRE-AUDIT** |
| 010 | `010_KOVARA_JIN` | Present | general DSR; Unit1 | **SELF-CERTIFIED / PRE-AUDIT** |
| 011 | `011_FOLKLORA_KURMANCA_1936` | Present | general DSR; Unit1 | **SELF-CERTIFIED / PRE-AUDIT** |
| 012 | `012_KURD_TEAVUN_TERAKKI_1908` | Present | general DSR; Unit1 | **SELF-CERTIFIED / PRE-AUDIT** |
| 013 | `013_ROJI_KURD_1913` | Present | general DSR; Unit1 | **SELF-CERTIFIED / PRE-AUDIT** |
| 014 | `014_DIROK_U_CIVAKA_KURDAN` | Present | general DSR; Unit1 | **SELF-CERTIFIED / PRE-AUDIT** |

### Corpus 008 filename preservation note
The committed files use `KOVARANAWAR` in filenames although the folder is `008_KOVARA_HAWAR`. Preserve the committed spelling for provenance unless a later explicit migration is performed with an audit record.

---

## Root Stage 4 artifacts from agent commit

- `TSLK_DISCOVERY_PROTOCOL_V1.md`
- `TSLK_DISCOVERY_PROTOCOL_V1.docx`
- `TSLK_METHODOLOGICAL_REPLICATION_AUDIT_V1.md`
- `TSLK_METHODOLOGICAL_REPLICATION_AUDIT_V1.docx`

Current status:

- root protocol: **SUPERSEDED AGENT-GENERATED METHOD DRAFT / PRESERVED**;
- root replication audit: **FAILED INDEPENDENT REVIEW / PRESERVED**.

The statement that Protocol V1 was “certified and validated across all 14 corpora” is not accepted.

---

## Independent audit failures already established

### Corpus 001
Layer A contains interpretive terminology including `Finite State/Action` and `D04_past`; target-set selection independence is not demonstrated; self-certification claims are therefore not accepted.

### Corpus 002 ANHA
D04 is defined using forms “exhibiting recurrent clause-final positioning” and M1 then tests clause-final positioning of that set. This is circular. Layer A also contains `suffix`, `Event/Action`, `Toponymic`, `Spatial/Locative`, and `Coordinator` terminology.

### Corpus 003 Ronahi
The same circular target-set/final-position architecture appears. Near-identical D01–D06 architecture across supposedly isolated corpora raises template-transfer risk requiring script/raw-evidence audit.

### Cross-corpus M1
Reported fit values of roughly 84%–97% across very different genres are treated as a **method-risk signal**, not a language finding, until target-set selection and unit-boundary effects are audited.

Full details:

`Research_Methods/Stage4_V1/TSLK_INDEPENDENT_AUDIT_FINDINGS.md`

---

## Mechanical audit infrastructure

Current extraction tool:

`Research_Methods/Stage4_V1/tools/extract_cstlk_text.py`

Current workflow:

`.github/workflows/extract-cstlk-text.yml`

Purpose: mechanically expose committed binary Word evidence as UTF-8 text with hashes and stable locators. Mechanical extraction must not perform linguistic interpretation.

The next infrastructure step is to expose DSR/LDR/report Word contents in the same auditable form so hidden item-level tables can be independently inspected.

---

## Audit gate before any full-corpus expansion

Full UNIT02/UNIT03 expansion is blocked until:

1. target-set selection provenance is known;
2. circular M1 tests are downgraded or rebuilt;
3. Layer A is genuinely neutral;
4. item-level audit tables are independently inspectable;
5. bounded-unit selection is source-appropriate and reproducible;
6. mechanical vs AI-judgment provenance is explicit;
7. at least a representative set of corpora is independently re-audited under the authoritative protocol;
8. Stream A remains isolated from Stream B.

---

## Current operational sequence

1. Preserve all agent artifacts exactly as committed.
2. Mechanically extract report DOCX content for independent inspection.
3. Audit Corpus 001 target-set construction and 88-item table.
4. Audit ANHA Unit1 source boundaries and 50-item table.
5. Audit Ronahi Unit1 and template-transfer risk.
6. Sample at least one pedagogical, historical-periodical, folklore, and monograph corpus.
7. Decide whether the next method version is V1.1 or V2 based on observed failures.
8. Only then resume bounded-unit expansion.
