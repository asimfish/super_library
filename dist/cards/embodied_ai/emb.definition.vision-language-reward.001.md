# Super Library card: emb.definition.vision-language-reward.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### vision-language reward

`emb.definition.vision-language-reward.001` · definition · embodied_ai, robot_learning, vision_language_action · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A dense reward or progress signal computed from a pretrained vision-language representation, typically the alignment between current observations and a goal given as language or an image, used to supervise control without hand-designed environment reward.

**Use:** State the pretraining data and objective, whether the signal is used as reward, value, or representation, and how goals are specified (language or image). Validate the signal against task success, since alignment scores can be exploited or miscalibrated.

**Avoid:** Do not treat vision-language alignment as ground-truth task progress without a success-based check, and do not conflate this observation-goal alignment signal with reward models fit to environment reward or with generative AI-feedback evaluators.

**Patterns:**

- The pretrained {vision-language model} assigns dense rewards as {alignment measure} between {observation} and {language or image goal}.
- We verify the learned reward against {task success metric} before policy training on {tasks}.

**Verify in primary sources:**

- `ma2023-liv-language-image-representations` — [LIV: Language-Image Representations and Rewards for Robotic Control](https://proceedings.mlr.press/v202/ma23b.html) (ICML 2023)
- `li2024-decisionnce-embodied-multimodal-representations` — [DecisionNCE: Embodied Multimodal Representations via Implicit Preference Learning](https://proceedings.mlr.press/v235/li24cr.html) (ICML 2024)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/vision_language_action.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: language_conditioned_control](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/language_conditioned_control.md)
- [topic: robot_foundation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/robot_foundation.md)
