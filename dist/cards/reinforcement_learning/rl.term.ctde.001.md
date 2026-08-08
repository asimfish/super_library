# Super Library card: rl.term.ctde.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### centralized training with decentralized execution (CTDE)

`rl.term.ctde.001` · term · reinforcement_learning · abstract, introduction, related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A multi-agent learning paradigm that permits access to joint or global information during training while each agent acts from locally available information at execution time.

**Use:** Specify what is centralized—critic, value, state, communication, or data—and what each deployed policy observes.

**Avoid:** Do not call execution decentralized if agents require unavailable global information at test time.

**Patterns:**

- We adopt CTDE: the centralized critic conditions on {joint information}, whereas each actor observes only {local information}.
- At execution time, agents act without {training-only signal}.

**Verify in primary sources:**

- `foerster2018coma` — [Counterfactual Multi-Agent Policy Gradients](https://ojs.aaai.org/index.php/AAAI/article/view/11794) (AAAI 2018)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: multi_agent_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/multi_agent_rl.md)
