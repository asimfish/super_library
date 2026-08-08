# Super Library card: emb.term.temporal-ensembling.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### temporal ensembling of overlapping action predictions

`emb.term.temporal-ensembling.001` · term · embodied_ai, robot_learning, vision_language_action · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

Combining action predictions made at different policy-query times for the same future control step.

**Use:** Describe the weighting function, overlap window, and whether aggregation occurs in action space or another representation. Mark ACT-specific weighting choices as implementation details rather than universal definitions.

**Avoid:** Do not confuse temporal ensembling with an ensemble of independently trained policies.

**Patterns:**

- At each control step, we aggregate overlapping action predictions using exponentially decaying weights.
- Temporal ensembling smooths predictions from successive action chunks.

**Verify in primary sources:**

- `zhao2023act` — [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://roboticsproceedings.org/rss19/p016.html) (RSS 2023)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/vision_language_action.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: action_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/action_representation.md)
