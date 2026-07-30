# Super Library card: emb.definition.action-chunking.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### action chunking

`emb.definition.action-chunking.001` · definition · embodied_ai, robot_learning, vision_language_action · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Predicting a block of consecutive future actions in one policy inference step rather than predicting only the next action.

**Use:** Report chunk length, execution or replanning frequency, overlap between chunks, and whether observations are incorporated again before the entire chunk is executed.

**Avoid:** Do not equate action chunking with open-loop execution; implementations may replan or aggregate overlapping chunks.

**Patterns:**

- The policy predicts a chunk of {k} future actions from the current observations.
- We replan every {n} control steps and combine overlapping action chunks with {aggregation rule}.

**Verify in primary sources:**

- `zhao2023act` — [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://roboticsproceedings.org/rss19/p016.html) (RSS 2023)
- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/robot_learning.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/vision_language_action.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: action_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/action_representation.md)
