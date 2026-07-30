# Super Library card: wm.usage-note.planning-vs-policy.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### online planning versus policy learning in imagination

`wm.usage-note.planning-vs-policy.001` · usage_note · world_models, reinforcement_learning · related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

World models may support decisions by optimizing actions at test time, by training an amortized policy on imagined experience, or by combining both.

**Use:** State when computation occurs and whether the deployed controller replans. This is a useful axis for organizing related work.

**Avoid:** Do not classify all world-model methods as planners.

**Patterns:**

- Whereas {method family} performs online planning in the learned model, {method family} trains a policy on imagined trajectories.
- Our method combines {online trajectory optimization} with {learned value or policy prior}.

**Verify in primary sources:**

- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/world_model_general.md)
- [topic: planning_imagination](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/planning_imagination.md)
