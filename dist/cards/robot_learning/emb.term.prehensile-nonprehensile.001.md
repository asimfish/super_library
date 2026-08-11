# Super Library card: emb.term.prehensile-nonprehensile.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### prehensile and non-prehensile manipulation

`emb.term.prehensile-nonprehensile.001` · term · robot_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Prehensile manipulation secures an object with a grasp, whereas non-prehensile manipulation changes object state through actions such as pushing without maintaining a grasp.

**Use:** Use the distinction to describe action primitives or coordination between them. Name the actual contact modes studied.

**Avoid:** Do not treat pushing as a failed grasp; it can be an intentional non-prehensile action.

**Patterns:**

- The policy coordinates prehensile grasping with non-prehensile pushing to {task objective}.
- Pushing changes the scene configuration before a grasp is attempted.

**Verify in primary sources:**

- `zeng2018pushgrasp` — [Learning Synergies Between Pushing and Grasping with Self-Supervised Deep Reinforcement Learning](https://ieeexplore.ieee.org/document/8593986/) (IROS 2018)

Catalog routes:
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: robot_manipulation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/robot_manipulation.md)
