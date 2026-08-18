# TSLK Stage 4 V1 Repository Manifest

## Status
**STAGE 4 V1 - REPOSITORY AUDIT IN PROGRESS**

This manifest records the actual committed GitHub state. It supersedes summaries that exist only in external/local agent workspaces.

Authoritative project context: `TSLK_PROJECT_CONTEXT.md`

Authoritative Stage 4 method: `Research_Methods/Stage4_V1/TSLK_DISCOVERY_PROTOCOL_V1.md`

Mechanical extraction tool: `Research_Methods/Stage4_V1/tools/extract_cstlk_text.py`

GitHub extraction workflow: `.github/workflows/extract-cstlk-text.yml`

---

## Status vocabulary

- `BASE COMMITTED`: CSTLK + LDR + Sources are present.
- `PRE-AUDIT DSR PRESENT`: a DSR artifact exists but has not yet passed Protocol V1 independent audit.
- `NO COMMITTED DSR`: no Stage 4 DSR artifact is currently committed in that corpus folder.
- `INVALIDATED/SUPERSEDED`: preserved for audit but excluded from the active evidence chain.
- `ACTIVE V1`: produced under the authoritative V1 protocol and independently audited.

No DSR is `ACTIVE V1` merely because its filename contains `UNIT1` or because an external agent described it as validated.

---

## Corpus inventory

| ID | Corpus folder | CSTLK corpus file | LDR file | Existing DSR state |
|---|---|---|---|---|
| 001 | `001_MEM_U_ZIN` | `CSTLK001MEMUZIN08172026FDA.docx` | `LDRSTLK001MEMUZIN08172026FDA.docx` | **NO COMMITTED DSR** |
| 002 | `002_ANHA` | `CSTLK002ANHA08172026FDA.docx` | `LDRSTLK002ANHA08172026FDA.docx` | **NO COMMITTED DSR** |
| 003 | `003_RONAHI` | `CSTLK003RONAHI08172026FDA.docx` | `LDRSTLK003RONAHI08172026FDA.docx` | **NO COMMITTED DSR** |
| 004 | `004_RUDAW` | `CSTLK004RUDAW08172026FDA.docx` | `LDRSTLK004RUDAW08172026FDA.docx` | **NO COMMITTED DSR** |
| 005 | `005_PIRTUKEN_KURMANCI_KATALOG` | `CSTLK005PIRTUKENKATALOG08172026FDA.docx` | `LDRSTLK005PIRTUKENKATALOG08172026FDA.docx` | **NO COMMITTED DSR** |
| 006 | `006_KURMANJI_BEGINNERS` | `CSTLK006KURMANJIBEGINNERS08172026FDA.docx` | `LDRSTLK006KURMANJIBEGINNERS08172026FDA.docx` | **NO COMMITTED DSR** |
| 007 | `007_KOVARA_KURMANCI` | `CSTLK007KOVARAKURMANCI08172026FDA.docx` | `LDRSTLK007KOVARAKURMANCI08172026FDA.docx` | **NO COMMITTED DSR** |
| 008 | `008_KOVARA_HAWAR` | `CSTLK008KOVARANAWAR08172026FDA.docx` | `LDRSTLK008KOVARANAWAR08172026FDA.docx` | **NO COMMITTED DSR** |
| 009 | `009_ROJNAMA_KURDISTAN` | `CSTLK009ROJNAMAKURDISTAN08172026FDA.docx` | `LDRSTLK009ROJNAMAKURDISTAN08172026FDA.docx` | **PRE-AUDIT DSR PRESENT**: `DSRSLK009ROJNAMAKURDISTAN08172026FDA.docx`; `DSRSLK009ROJNAMAKURDISTAN08172026FDA_UNIT1.docx` |
| 010 | `010_KOVARA_JIN` | `CSTLK010KOVARA_JIN08172026FDA.docx` | `LDRSTLK010KOVARA_JIN08172026FDA.docx` | **PRE-AUDIT DSR PRESENT**: `DSRSLK010KOVARA_JIN08172026FDA.docx`; `DSRSLK010KOVARA_JIN08172026FDA_UNIT1.docx` |
| 011 | `011_FOLKLORA_KURMANCA_1936` | `CSTLK011FOLKLORAKURMANCA193608172026FDA.docx` | `LDRSTLK011FOLKLORAKURMANCA193608172026FDA.docx` | **PRE-AUDIT DSR PRESENT**: `DSRSLK011FOLKLORAKURMANCA193608172026FDA.docx`; `DSRSLK011FOLKLORAKURMANCA193608172026FDA_UNIT1.docx` |
| 012 | `012_KURD_TEAVUN_TERAKKI_1908` | `CSTLK012KURDTEAVUNTERAKKI190808172026FDA.docx` | `LDRSTLK012KURDTEAVUNTERAKKI190808172026FDA.docx` | **PRE-AUDIT DSR PRESENT**: `DSRSLK012KURDTEAVUNTERAKKI190808172026FDA.docx`; `DSRSLK012KURDTEAVUNTERAKKI190808172026FDA_UNIT1.docx` |
| 013 | `013_ROJI_KURD_1913` | `CSTLK013ROJIKURD191308172026FDA.docx` | `LDRSTLK013ROJIKURD191308172026FDA.docx` | **PRE-AUDIT DSR PRESENT**: `DSRSLK013ROJIKURD191308172026FDA.docx`; `DSRSLK013ROJIKURD191308172026FDA_UNIT1.docx` |
| 014 | `014_DIROK_U_CIVAKA_KURDAN` | `CSTLK014DIROKUCIVAKAKURDAN08172026FDA.docx` | `LDRSTLK014DIROKUCIVAKAKURDAN08172026FDA.docx` | **PRE-AUDIT DSR PRESENT**: `DSRSLK014DIROKUCIVAKAKURDAN08172026FDA.docx`; `DSRSLK014DIROKUCIVAKAKURDAN08172026FDA_UNIT1.docx` |

### Filename preservation note
The committed files under Corpus 008 contain `KOVARANAWAR` in the filename although the folder is `008_KOVARA_HAWAR`. This manifest records the committed filename exactly. No silent renaming/correction is authorized during provenance-sensitive research.

---

## Current audit decision

### Corpora 001-008
No committed Stage 4 DSR is currently available in the corpus folder. External-agent reports about local Unit 1 files are not treated as committed research evidence.

### Corpora 009-014
Existing DSR/UNIT1 DOCX files are preserved, but their methodological status is **PRE-AUDIT**. Until their contents are extracted and inspected against Protocol V1, they must not be used as evidence for later grammar reconstruction or cross-corpus comparison.

---

## Mechanical extraction plan

The repository now includes a GitHub-native extraction system designed to make the binary CSTLK Word documents directly auditable as UTF-8 text.

Expected generated root:

`Research_Extracts/Stage4_V1/`

For each corpus the extraction package should contain:

- `CSTLK...__MECHANICAL_EXTRACT.txt`
- `CSTLK...__MECHANICAL_EXTRACT.jsonl`

and the root extraction manifest:

- `MECHANICAL_EXTRACTION_MANIFEST.json`

The extraction process is mechanical only. It must not translate, normalize, segment linguistically, classify grammatical categories, or assign meanings.

---

## Stage 4 audit gate

Before full-corpus expansion, the following must be true:

1. committed CSTLK text is directly inspectable in GitHub;
2. bounded-unit selection rules are explicit and source-appropriate;
3. Layer A contains only observation;
4. Layer B hypotheses are traceable to Layer A;
5. no known Kurdish grammar is used as evidence;
6. all form/class selection criteria are exposed;
7. mathematical tests are non-circular or explicitly marked descriptive-only;
8. every fit metric exposes the full denominator and item-level classifications;
9. scripts are limited to mechanical operations;
10. existing DSR files are classified as active, superseded, or invalidated only after content audit.

---

## Research streams

Stream A documentary analysis remains isolated from Stream B native-speaker work. No Ferhad-supplied meanings, spoken examples, or pronunciation judgments may be used to repair or confirm Stage 4 corpus hypotheses until the later explicitly authorized comparison phase.

---

## Next repository-native operation

1. obtain searchable mechanical extracts of committed CSTLK corpora;
2. inspect Corpus 001 as the first V1 evidence audit;
3. separately inspect existing pre-audit DSRs in 009-014;
4. produce new V1 bounded-unit studies only from the committed primary/corpus evidence;
5. preserve every prior state.
