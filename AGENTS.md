# Kurdish-TSL Agent Contract

## Project objective
Kurdish-TSL is currently in a **grammar-discovery phase**. The immediate task is not to apply an existing description of Kurmancî grammar. The task is to recover trustworthy corpus text, observe recurrent structure, propose hypotheses from corpus evidence, and test those hypotheses across independent texts.

## Non-negotiable rule: corpus evidence before grammar knowledge
During discovery work, agents MUST NOT use remembered, learned, retrieved, or textbook Kurdish/Kurmancî grammar as evidence for an analysis.

Agents may know Kurdish grammar internally, but they must quarantine that knowledge. A statement is admissible in the discovery record only when it can be supported by the project corpus itself.

Do not begin from categories such as case, ezafe, ergativity, tense, aspect, mood, clitic, gender, agreement, noun, verb, subject, object, or any other inherited grammatical label unless the corpus evidence has already justified introducing that label. Early-stage labels should be neutral and descriptive, e.g. FORM-001, PATTERN-A, SLOT-2, SERIES-X.

## Evidence classes
Every analytical statement must be marked as one of:

1. **OBSERVED** — directly present in a cited corpus passage.
2. **INFERRED** — a generalization proposed from multiple observations.
3. **EXTERNAL** — knowledge from outside the corpus. External knowledge is excluded from discovery decisions unless the project explicitly enters a later comparison phase.

Never silently convert EXTERNAL knowledge into OBSERVED or INFERRED claims.

## Required phase order

### Phase 0 — Source preservation and provenance
- Preserve source documents unchanged.
- Record source identity, date/edition when known, script, extraction method, and uncertainty.
- Never overwrite the only copy of a source.

### Phase 1 — Text recovery
Goal: produce the clearest faithful text possible.
- Correct only demonstrable OCR/encoding/layout corruption.
- Preserve uncertain readings explicitly.
- Do not normalize a form merely because another spelling is expected.
- Do not rewrite historical, dialectal, editorial, or source-specific forms into a preferred standard.

### Phase 2 — Observation
- Extract repeated strings, alternations, local contexts, positional behavior, co-occurrence patterns, boundary behavior, and distribution.
- Cite exact examples and source locations.
- Use neutral labels.
- Record exceptions and counterexamples immediately.

### Phase 3 — Hypothesis formation
- Propose the smallest rule that explains the observations.
- State what evidence supports it.
- State what evidence would falsify it.
- Assign provisional confidence.
- Keep competing hypotheses when evidence does not decide between them.

### Phase 4 — Cross-corpus testing
- Test hypotheses against texts from different genres, dates, authors, and sources.
- Distinguish productive patterns from source-specific, historical, editorial, lexical, or noisy phenomena.
- Search actively for counterexamples.

### Phase 5 — Grammar synthesis
Only after repeated cross-corpus support may stable descriptive categories and rules be introduced. Each rule must retain an evidence trail back to corpus examples.

### Phase 6 — External comparison and implementation
Textbook grammars, published linguistic literature, parsers, morphological analyzers, and program implementation belong here unless the project owner explicitly changes the phase.

## Current prohibition on premature implementation
Do not write a grammar engine, parser, morphological analyzer, tagging program, or rule-based implementation while the project is still discovering the grammar. Scripts that mechanically preserve, extract, index, count, or search the corpus are allowed only if they do not encode grammatical assumptions.

## Legacy diagnosis documents
Files whose names contain `LDRSTLK`, files in `Linguistic_Diagnosis_Reports/`, and the current master grammar document are **legacy/preliminary analyses**. They may be archived for later comparison, but they must not be used as evidence during discovery because they may contain prior grammatical assumptions.

## Minimum evidence record for every proposed pattern
Record:
- corpus/source ID;
- exact passage or recoverable location;
- observed form(s);
- local context;
- neutral pattern label;
- supporting examples;
- counterexamples;
- alternative explanations;
- confidence;
- status: observed / candidate / supported / rejected / unresolved.

## Manager responsibility
The manager agent must enforce phase boundaries, prevent prior-grammar leakage, require evidence citations, preserve unresolved alternatives, and stop subordinate agents from turning tentative patterns into facts.
