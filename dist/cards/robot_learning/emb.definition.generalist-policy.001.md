# Super Library card: emb.definition.generalist-policy.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### generalist robot policy

`emb.definition.generalist-policy.001` · definition · robot_learning, embodied_ai · abstract, introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A policy trained across diverse tasks, environments, or robot data with the aim of supporting multiple behaviors and transfer beyond a single narrowly trained task.

**Use:** State the diversity actually represented in training and evaluation. Distinguish multi-task performance, zero-shot generalization, and fine-tuning ability.

**Avoid:** Do not call a policy generalist solely because one architecture is reused across several separately trained tasks.

**Patterns:**

- We train a generalist robot policy on {tasks, environments, and embodiments}.
- We separately evaluate in-distribution multi-task performance and transfer to {new setting}.

**Verify in primary sources:**

- `brohan2023rt1` — [RT-1: Robotics Transformer for Real-World Control at Scale](https://roboticsproceedings.org/rss19/p025.html) (RSS 2023)
- `ghosh2024octo` — [Octo: An Open-Source Generalist Robot Policy](https://www.roboticsproceedings.org/rss20/p090.html) (RSS 2024)
- `khazatsky2024droid` — [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://roboticsproceedings.org/rss20/p120.html) (RSS 2024)

Catalog routes:
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: robot_foundation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/robot_foundation.md)
