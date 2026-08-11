# Super Library card: rl.definition.credit-assignment.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### multi-agent credit assignment

`rl.definition.credit-assignment.001` · definition · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

The problem of determining how individual agents' actions contribute to a shared outcome so that each policy receives an informative learning signal.

**Use:** State whether credit is temporal, agent-specific, or both. Explain the baseline or decomposition used to isolate an agent's contribution.

**Avoid:** Do not equate a global team reward with solved credit assignment.

**Patterns:**

- A counterfactual baseline improves credit assignment by comparing an agent's chosen action with {alternative actions} while holding {other agents} fixed.
- The shared reward provides weak agent-specific credit in {setting}.

**Verify in primary sources:**

- `foerster2018coma` — [Counterfactual Multi-Agent Policy Gradients](https://ojs.aaai.org/index.php/AAAI/article/view/11794) (AAAI 2018)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: multi_agent_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/multi_agent_rl.md)
