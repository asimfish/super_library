# Super Library card: rl.definition.ai-feedback.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### AI feedback

`rl.definition.ai-feedback.001` · definition · reinforcement_learning, embodied_ai · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A training signal, such as rewards, preferences, or critiques, produced by a separate pretrained model that evaluates the learner's behavior, used in place of or in addition to environment reward or human feedback.

**Use:** Identify the evaluator model, what it scores, and how often it is queried; state how its judgments are validated and how exploitation of evaluator weaknesses is detected. Keep AI feedback distinct from reward models fit to environment reward and from direct human feedback.

**Avoid:** Do not present evaluator scores as ground-truth task success, and do not report gains from AI feedback without stating the evaluator's known failure modes.

**Patterns:**

- A {evaluator model} scores {agent behavior}, and the score is used as {reward or preference signal} during training.
- We validate AI feedback against {human labels or task metrics} on {validation set}.

**Verify in primary sources:**

- `li2025-larm-large-auto-regressive` — [LARM: Large Auto-Regressive Model for Long-Horizon Embodied Intelligence](https://proceedings.mlr.press/v267/li25dj.html) (ICML 2025)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: embodied_reasoning_agents](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/embodied_reasoning_agents.md)
- [topic: policy_optimization](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/policy_optimization.md)
