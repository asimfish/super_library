# Super Library card: rl.definition.self-supervised-representation-learning.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### self-supervised representation learning

`rl.definition.self-supervised-representation-learning.001` · definition · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Training an observation encoder with auxiliary objectives derived from the data itself, such as correspondence, prediction, or consistency targets, instead of relying only on reward or temporal-difference signals to shape the representation.

**Use:** Name the auxiliary objective and the structure it captures (local correspondence, global semantics, or future prediction), and state how representation learning interacts with policy or value training, including whether the two are decoupled or alternated for stability.

**Avoid:** Do not describe reward-driven end-to-end encoder training as self-supervised, and do not claim representation quality from task return alone.

**Patterns:**

- The encoder is trained with {auxiliary objective} that enforces {structural constraint} across {frames or views}.
- Representation and policy learning are {decoupled or alternated} to prevent instability induced by {bootstrapped targets}.

**Verify in primary sources:**

- `choi2023-local-guided-global-paired` — [Local-Guided Global: Paired Similarity Representation for Visual Reinforcement Learning](https://openaccess.thecvf.com/content/CVPR2023/html/Choi_Local-Guided_Global_Paired_Similarity_Representation_for_Visual_Reinforcement_Learning_CVPR_2023_paper.html) (CVPR 2023)
- `zhai2023-stabilizing-visual-reinforcement-learning` — [Stabilizing Visual Reinforcement Learning via Asymmetric Interactive Cooperation](https://openaccess.thecvf.com/content/ICCV2023/html/Zhai_Stabilizing_Visual_Reinforcement_Learning_via_Asymmetric_Interactive_Cooperation_ICCV_2023_paper.html) (ICCV 2023)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: dynamics_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/dynamics_representation.md)
