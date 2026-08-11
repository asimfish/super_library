# Super Library card: rl.definition.pomdp.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### partially observable Markov decision process (POMDP)

`rl.definition.pomdp.001` · definition · reinforcement_learning · method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A sequential decision process in which observations do not fully reveal the underlying state, specified by states, actions, transition dynamics, rewards, and an observation model, so optimal behavior may depend on the interaction history or a belief over states.

**Use:** State the observation model and what the agent conditions on (history, belief, or a learned latent state). Say which quantities are unobserved and whether evaluation assumes privileged state access. Reserve plain MDP language for fully observed settings.

**Avoid:** Do not analyze a partially observed system under fully observed MDP assumptions, and do not use POMDP loosely for any difficult RL problem.

**Patterns:**

- We model the task as a POMDP in which {unobserved factor} is hidden and the agent receives only {observation}.
- The policy conditions on {history or belief representation} rather than on the underlying state.

**Verify in primary sources:**

- `hong2024-model-based-reinforcement-learning` — [Model-based Reinforcement Learning for Confounded POMDPs](https://proceedings.mlr.press/v235/hong24d.html) (ICML 2024)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/rl_theory_evaluation.md)
