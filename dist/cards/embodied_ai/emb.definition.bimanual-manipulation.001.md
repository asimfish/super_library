# Super Library card: emb.definition.bimanual-manipulation.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### bimanual robotic manipulation

`emb.definition.bimanual-manipulation.001` · definition · embodied_ai, robot_learning, vision_language_action · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Manipulation in which two robot arms or end effectors must act in a coordinated manner to accomplish a task.

**Use:** Specify whether coordination is symmetric or asymmetric, the control space for each arm, sensing, synchronization, and the task phase requiring coordination.

**Avoid:** Do not call independent single-arm subtasks bimanual coordination unless their actions are coupled by the object or objective.

**Patterns:**

- The benchmark contains contact-rich bimanual tasks that require coordinated motion of both end effectors.
- The policy jointly predicts left- and right-arm actions at {frequency} Hz.

**Verify in primary sources:**

- `zhao2023act` — [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://roboticsproceedings.org/rss19/p016.html) (RSS 2023)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/vision_language_action.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: robot_manipulation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/robot_manipulation.md)
