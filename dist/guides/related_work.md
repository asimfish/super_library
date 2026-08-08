# Super Library protocol: Related Work: evidence-verified synthesis and positioning

`related_work` · `section_protocol` · section `related_work` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results.

Organize verified primary papers into problem-relevant families, compare them on explicit axes, and locate the present work without paper-by-paper narration or unsupported priority claims.

**Use when:** Planning, drafting, or revising an AI-paper Related Work section or a focused literature-positioning paragraph.

## Required inputs

- The exact task, setting, and claim that the literature discussion must contextualize.
- Verified primary papers with bibliographic metadata and notes tied to specific passages.
- A small set of organizing families and explicit comparison axes such as objective, supervision, data regime, assumptions, compute, or deployment setting.
- The present paper's factual relationship to each relevant family, including shared assumptions and material differences.

## Functional protocol

### 1. Verify the literature evidence (required)

- Open every primary paper used for a definition, historical claim, method characterization, or comparison.
- Record what the cited passage supports and do not infer absent limitations from silence.
- Use the library's source IDs only as navigation; never treat a corpus summary as the citation evidence.

### 2. Build a task-relevant taxonomy (required)

- Group papers by the technical choice that matters to this paper rather than by arbitrary chronology.
- State the comparison axis before naming examples from a family.
- Separate families that solve different problem settings instead of ranking them together.

### 3. Synthesize similarities and differences (required)

- Describe a recurring approach, then identify a verified assumption, mechanism, or scope difference.
- Make the subject of every evaluative statement explicit: method, dataset, protocol, or result.
- Distinguish reported evidence from the authors' interpretation and from this paper's synthesis.

### 4. Position the present work precisely (required)

- State what is shared with prior work before the differentiating axis.
- Name the changed assumption, supervision, data, mechanism, evaluation, or deployment constraint.
- Do not imply superiority unless a verified comparable experiment supports it.

## Choose one internal template

### Taxonomy-first synthesis

Use when: Several approach families address a common task under different assumptions.

1. Define the shared task and organizing axis.
2. Describe the first family and its operative assumption.
3. Contrast the next family on the same axis.
4. Synthesize the unresolved boundary across families.
5. Position the present work on that boundary.

### Concept evolution

Use when: Chronology is scientifically meaningful because later work changes a specific assumption or capability.

1. State the original formulation or capability with a primary source.
2. Describe the verified change introduced by subsequent work.
3. Compare the resulting families on a stable axis rather than merely listing years.
4. Identify the remaining problem addressed here.

## Verification

- Every citation exists, has been opened, and supports the adjacent proposition at the stated scope.
- Every comparison names a common axis and avoids ranking incompatible protocols.
- Definitions are paraphrases unless a short quotation is explicitly marked and permitted.
- The section represents close alternatives fairly, including assumptions that favor the present method.
- No claim uses latest, first, only, most, or state-of-the-art without a separately verified comparison set.

## Avoid

- One sentence per paper with no cross-paper synthesis.
- Citation clusters whose individual sources do not support the whole sentence.
- Describing prior work only through limitations while omitting its intended setting or strength.
- Using temporal recency as a proxy for relevance, quality, or novelty.

## Retrieve related sentence cards only as needed

- [A complementary line of work studies {adjacent problem}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.related-family.001.md) — `general.sentence-pattern.related-family.001`
- [These approaches share {common objective}, but differ in {technical axes}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.related-synthesis.001.md) — `general.sentence-pattern.related-synthesis.001`
- [Prior approaches differ primarily in {axis one} and {axis two}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.position.001.md) — `general.sentence-pattern.position.001`
- [Unlike {comparison class}, which {defining behavior}, our approach {distinct behavior}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.contrast.001.md) — `general.sentence-pattern.contrast.001`
- [Distinguish possibility, interpretation, empirical evidence, and formal proof.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.modality.001.md) — `general.usage-note.modality.001`
- [state-of-the-art performance on {benchmark} under {protocol}](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.state-of-the-art.001.md) — `general.usage-note.state-of-the-art.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.
