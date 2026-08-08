# Super Library universal core

Corpus `0.4.0` · contract `4.0` · snapshot `2026-08-09`.

Read this once, then return to the [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) and load only selected cards.

## Non-negotiable contract

1. Preserve the user's scientific propositions, numbers, equations,
   citations, negation, comparison direction, and epistemic uncertainty.
2. Retrieve rhetoric by section/intent and terminology by technical domain
   without a section filter. Do not use one query for both jobs.
3. Prefer field-standard terms and short attested collocations. Treat original
   sentence patterns as structural guardrails and rewrite them for the paper.
4. Reopen primary sources before making definitions, historical statements,
   method comparisons, or Related Work claims. Never invent metadata.
5. In rebuttals, answer first and use only existing evidence. If evidence is
   missing, narrow the claim instead of inventing an experiment.
6. In translation, reconstruct the proposition rather than Chinese word order.
7. Use `state-of-the-art` and statistical-significance language only when the
   required comparison or inferential evidence is present.

## Essential records

### Prior approaches differ primarily in {axis one} and {axis two}.

`general.sentence-pattern.position.001` · `sentence_pattern` · `original_pattern`

Organizes related work by technical comparison axes instead of paper-by-paper chronology.

**Use:** Choose axes that expose meaningful assumptions or design choices, then place representative methods along them with citations.

**Avoid:** Do not invent a taxonomy whose categories overlap without explanation.

**Pattern:** Prior approaches differ primarily in how they {technical axis one} and whether they {technical axis two}.

### {method} improves {metric} by {value} relative to {baseline} under {protocol}.

`general.sentence-pattern.quantify.001` · `sentence_pattern` · `original_pattern`

Reports a quantified comparison with its baseline and protocol.

**Use:** State whether the value is absolute or relative, and match the aggregation and uncertainty used in the table.

**Avoid:** Avoid 'significant' unless statistical significance was actually tested.

**Pattern:** {method} improves mean {metric} by {absolute or relative value} over {baseline} under the {protocol} protocol.

### These results are consistent with the hypothesis that {mechanism}.

`general.sentence-pattern.causal-caution.001` · `sentence_pattern` · `original_pattern`

Links observations to a mechanism without claiming that the experiment identifies causality.

**Use:** Use when evidence supports but does not isolate the proposed explanation. Follow with an ablation or limitation if available.

**Avoid:** Do not write 'the gains are due to' without an identifying intervention.

**Pattern:** These results are consistent with the hypothesis that {component or inductive bias} improves {measured behavior}.

### For a controlled comparison, we hold {factor} fixed and vary only {factor}.

`general.sentence-pattern.fair-comparison.001` · `sentence_pattern` · `original_pattern`

Explains how an experiment isolates a comparison dimension.

**Use:** Use only when the protocol truly controls the named factor; list remaining mismatches if they affect interpretation.

**Avoid:** Do not call a comparison controlled when data, compute, architecture, or tuning differs materially.

**Pattern:** For a controlled comparison, we hold {data and compute budget} fixed and vary only {model component}.

### Our evaluation is limited to {scope}; performance under {unseen condition} remains to be established.

`general.sentence-pattern.limitation.001` · `sentence_pattern` · `original_pattern`

States an evaluation boundary and separates tested from untested conditions.

**Use:** Name the missing population, environment, scale, horizon, embodiment, or distribution. Do not bury a material limitation.

**Avoid:** Do not turn a limitation into an unsupported claim that future work will certainly solve it.

**Pattern:** Our evaluation is limited to {tasks or environments}; robustness to {shift} remains to be established.

### Yes. {direct answer}; the supporting evidence is {evidence pointer}.

`general.sentence-pattern.rebuttal-answer.001` · `sentence_pattern` · `original_pattern`

Answers a reviewer question immediately and then points to evidence.

**Use:** Use when the answer is genuinely yes. Replace the first token with 'No' or a qualified answer when appropriate; never force agreement.

**Avoid:** Do not begin with a long thank-you paragraph that delays the answer.

**Pattern:** Yes. {claim bounded to the question}; the supporting evidence is reported in {table, figure, section, or verified result}.

### The requested comparison is already included in {location}, where {verified result}.

`general.sentence-pattern.rebuttal-evidence.001` · `sentence_pattern` · `original_pattern`

Points a reviewer to existing evidence and summarizes only the relevant result.

**Use:** Give an exact manuscript location and reproduce numbers faithfully. If absent, use a revision or limitation frame instead.

**Avoid:** Do not invent a table location or imply that an indirect analysis answers the request.

**Pattern:** The requested comparison is already included in {Table or Appendix}, where {method} achieves {verified metric} under {protocol}.

### We will revise {location} to make {point} explicit.

`general.sentence-pattern.rebuttal-revision.001` · `sentence_pattern` · `original_pattern`

Commits to a concrete presentation change in response to feedback.

**Use:** Name the section, statement, figure, caption, or experimental detail and the information to add. Do not promise a new result unless it exists.

**Avoid:** Avoid vague promises such as 'we will improve the paper.'

**Pattern:** We will revise {Section or caption} to make {assumption, protocol, or limitation} explicit.

### We do not currently have evidence for {broader claim}; we will restrict the manuscript to {supported claim}.

`general.sentence-pattern.rebuttal-no-evidence.001` · `sentence_pattern` · `original_pattern`

Responds to a request that cannot be supported with existing results by narrowing the claim instead of inventing evidence.

**Use:** Use when the requested experiment was not run or the available analysis is insufficient. Explain what existing evidence still supports.

**Avoid:** Do not imply that an unrun experiment produced a favorable result or promise a result whose outcome is unknown.

**Pattern:** We do not currently have evidence for robustness under {shift}; we will restrict the manuscript to the evaluated {scope}.

### Although {qualified premise}, {bounded conclusion}.

`general.sentence-pattern.translation-preserve.001` · `sentence_pattern` · `original_pattern`

Preserves a concession and its qualification during Chinese-to-English reconstruction.

**Use:** Keep negation, modality, comparison direction, quantities, and citations attached to the same propositions as in the source.

**Avoid:** Do not upgrade a qualified Chinese claim into an unconditional English conclusion.

**Pattern:** Although {method} improves {metric} on {subset}, the difference is not statistically significant across {units}.

### Distinguish possibility, interpretation, empirical evidence, and formal proof.

`general.usage-note.modality.001` · `usage_note` · `original_pattern`

Modal verbs and evidential verbs serve different functions rather than forming one universal strength ordering.

**Use:** Use 'may/might' for possibility, 'suggests/supports' for a tentative interpretation or evidence relation, 'shows/demonstrates' for a result established within the study design, and 'proves' only for a formal proof under stated assumptions.

**Avoid:** Do not translate 可能 or 表明 into an unqualified 'proves', or assume that any two evidential verbs have a context-free ordering.

**Pattern:** The results suggest that {hypothesis}, but do not establish {stronger causal claim}.

### state-of-the-art performance on {benchmark} under {protocol}

`general.usage-note.state-of-the-art.001` · `usage_note` · `original_pattern`

A scoped claim that a verified result is best within a defined comparison set.

**Use:** Use only after checking the benchmark, metric, split, protocol, contemporaneous comparison set, and direction of improvement. Prefer the exact result when the scope is narrow.

**Avoid:** Never use 'state-of-the-art' as a general adjective for the method or as a synonym for strong.

**Pattern:** Under the {protocol} protocol, {method} achieves the best reported {metric} among {comparison set}.

### statistically significant versus substantial improvement

`general.usage-note.significant.001` · `usage_note` · `original_pattern`

Statistical significance refers to an inferential test or interval criterion, whereas substantial, marked, or large describes effect magnitude and requires a stated scale.

**Use:** Translate 显著 according to evidence: use 'statistically significant' only when a specified statistical analysis supports it; otherwise report the effect size or use a magnitude term justified by context.

**Avoid:** Do not infer statistical significance from a visibly larger mean, non-overlapping point estimates, or the Chinese adjective 显著 alone.

**Pattern:** {method} yields a {value}-point improvement, but the difference is not statistically significant under {test}.

### replace vague effectiveness claims with the observed outcome

`general.usage-note.effectiveness.001` · `usage_note` · `original_pattern`

An effectiveness claim is informative only when it names the intervention, comparison, metric, and evaluated setting.

**Use:** Write the measured change directly. Use 'supports the effectiveness of' only when several results jointly justify the scoped judgment; use 'proves' only for a formal result.

**Avoid:** Avoid 'the experiments prove the effectiveness and superiority of our method.'

**Pattern:** Across {tasks}, {method} improves {metric} over {baselines} under a matched {budget}.

### name the generalization axis and held-out unit

`general.usage-note.generalization-axis.001` · `usage_note` · `original_pattern`

Generalization is always relative to a specified shift, such as unseen objects, tasks, environments, users, embodiments, or combinations.

**Use:** State what was held out during training and what unit is averaged at evaluation. Prefer 'generalization to unseen objects' over an unqualified 'generalization ability.'

**Avoid:** Do not infer broad out-of-distribution generalization from a random train–test split over nearly identical samples.

**Pattern:** We evaluate generalization to unseen {objects or tasks} by holding out {unit} during training.
