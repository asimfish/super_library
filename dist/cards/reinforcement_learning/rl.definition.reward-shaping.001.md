# Super Library card: rl.definition.reward-shaping.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### reward shaping

`rl.definition.reward-shaping.001` · definition · reinforcement_learning, embodied_ai · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Modifying or augmenting the task reward with additional signals, such as progress terms or auxiliary bonuses, to densify feedback and accelerate learning, ideally without changing the optimal policy of the original objective.

**Use:** State what is added to the terminal or task reward, whether shaping preserves optimal behavior (for example potential-based forms), and the engineering effort it requires; compare against learning from unshaped terminal rewards when feasible.

**Avoid:** Do not present shaped-reward results as evidence the task is solvable from terminal rewards alone, and do not leave shaping terms undisclosed when they change the effective objective.

**Patterns:**

- We augment the terminal reward with {shaping signal}, which preserves {optimality property}.
- From terminal rewards alone, performance drops to {value}, motivating {shaping or teacher scheme}.

**Verify in primary sources:**

- `jain2021-gridtopix-training-embodied-agents` — [GridToPix: Training Embodied Agents With Minimal Supervision](https://openaccess.thecvf.com/content/ICCV2021/html/Jain_GridToPix_Training_Embodied_Agents_With_Minimal_Supervision_ICCV_2021_paper.html) (ICCV 2021)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: policy_optimization](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/policy_optimization.md)
