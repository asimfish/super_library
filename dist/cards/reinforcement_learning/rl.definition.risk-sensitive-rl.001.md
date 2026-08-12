# Super Library card: rl.definition.risk-sensitive-rl.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### risk-sensitive reinforcement learning

`rl.definition.risk-sensitive-rl.001` · definition · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A formulation that optimizes a risk measure of the return distribution, such as CVaR or other tail-sensitive criteria, instead of expected return, so policies trade average performance for protection against poor outcomes.

**Use:** Name the risk measure and its level, state whether risk applies to returns or per-step costs, and report both the risk metric and expected return. Say how the method avoids the conservatism or local-optimum pathologies of ignoring high-return behavior.

**Avoid:** Do not use risk-sensitive as a synonym for safe RL with explicit constraints, and do not report improved tail metrics without disclosing the change in expected return.

**Patterns:**

- We optimize {risk measure} at level {alpha} of the return distribution instead of expected return.
- The learned policy improves {tail metric} while retaining {fraction} of the risk-neutral return on {tasks}.

**Verify in primary sources:**

- `bastani2022-regret-bounds-risk-sensitive` — [Regret Bounds for Risk-Sensitive Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2022/hash/eb4898d622e9a48b5f9713ea1fcff2bf-Abstract-Conference.html) (NeurIPS 2022)
- `greenberg2022-efficient-risk-averse-reinforcement` — [Efficient Risk-Averse Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2022/hash/d2511dfb731fa336739782ba825cd98c-Abstract-Conference.html) (NeurIPS 2022)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: safe_robust_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/safe_robust_rl.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/rl_theory_evaluation.md)
