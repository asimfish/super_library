# Super Library card: rl.definition.skill-discovery.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### unsupervised skill discovery

`rl.definition.skill-discovery.001` · definition · reinforcement_learning · introduction, related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

The learning of a diverse set of temporally extended behaviors without task-specific external rewards, typically by optimizing an intrinsic diversity or predictability objective.

**Use:** State the skill variable, intrinsic objective, temporal horizon, diversity measure, and downstream adaptation protocol.

**Avoid:** Do not equate visually different trajectories with useful or controllable skills without a downstream criterion.

**Patterns:**

- The agent learns a skill-conditioned policy by maximizing {intrinsic objective} over {skill distribution} before downstream adaptation.

**Verify in primary sources:**

- `chalumeau2023-neuroevolution-competitive-alternative-reinforcement` — [Neuroevolution is a Competitive Alternative to Reinforcement Learning for Skill Discovery](https://iclr.cc/virtual/2023/poster/10722) (ICLR 2023)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [topic: exploration_skills_goals](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/exploration_skills_goals.md)
