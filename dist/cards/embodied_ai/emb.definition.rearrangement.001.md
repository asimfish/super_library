# Super Library card: emb.definition.rearrangement.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### object rearrangement

`emb.definition.rearrangement.001` · definition · embodied_ai, robot_learning · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

An embodied task family in which an agent changes the state of an environment to a specified goal configuration by locating, picking, moving, and placing objects, typically combining navigation with manipulation over long horizons.

**Use:** Specify the goal-specification format, the skills composed (navigate, pick, place), success criteria per stage and overall, and whether the setting is simulated or real. Report stage-wise failures because long-horizon success compounds errors.

**Avoid:** Do not report single-skill results as rearrangement, and do not omit the goal-specification format, since geometric, semantic, and language goals differ in difficulty.

**Patterns:**

- The agent rearranges {objects} from {initial configuration} to {goal specification} by composing {skills}.
- We report per-stage success for {navigate, pick, place} together with end-to-end success on {benchmark}.

**Verify in primary sources:**

- `berges2023-galactic-scaling-end-end` — [Galactic: Scaling End-to-End Reinforcement Learning for Rearrangement at 100k Steps-per-Second](https://openaccess.thecvf.com/content/CVPR2023/html/Berges_Galactic_Scaling_End-to-End_Reinforcement_Learning_for_Rearrangement_at_100k_Steps-per-Second_CVPR_2023_paper.html) (CVPR 2023)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: robot_manipulation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/robot_manipulation.md)
- [topic: embodied_navigation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/embodied_navigation.md)
