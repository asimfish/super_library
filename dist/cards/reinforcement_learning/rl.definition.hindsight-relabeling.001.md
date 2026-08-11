# Super Library card: rl.definition.hindsight-relabeling.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### hindsight relabeling

`rl.definition.hindsight-relabeling.001` · definition · reinforcement_learning, robot_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Reusing collected trajectories by replacing the intended goal with a goal actually achieved in hindsight, so failed episodes still supply positive examples for goal-conditioned learning without new environment interaction or manual reward design.

**Use:** State the relabeling distribution (final state, future states, or learned goals), the fraction of relabeled data, and how relabeled rewards are computed. Note interactions with offline settings where support constraints still apply.

**Avoid:** Do not present hindsight relabeling as a general fix for exploration; it only densifies learning signal for goals already covered by collected behavior.

**Patterns:**

- Transitions are relabeled with goals sampled from {relabeling distribution}, turning failures into positive examples for {learned quantity}.
- We combine hindsight relabeling with {method} to learn {skill set} from reward-free offline data.

**Verify in primary sources:**

- `chebotar2021-actionable-models-unsupervised-offline` — [Actionable Models: Unsupervised Offline Reinforcement Learning of Robotic Skills](https://proceedings.mlr.press/v139/chebotar21a.html) (ICML 2021)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: exploration_skills_goals](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/exploration_skills_goals.md)
- [topic: offline_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/offline_rl.md)
