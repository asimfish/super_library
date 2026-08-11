# Super Library card: vla.term.action-vocabulary.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### action vocabulary / action-token vocabulary

`vla.term.action-vocabulary.001` · term · vision_language_action, robot_learning · abstract, introduction, related_work, method

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The discrete set of symbols used to encode robot actions when a policy casts action prediction as token generation.

**Use:** State how continuous controls are quantized, which action dimensions are covered, and whether the vocabulary is shared across embodiments.

**Avoid:** Do not imply that discretization is inherent to all VLA models; many policies retain continuous action heads.

**Patterns:**

- We quantize {action dimensions} into an action vocabulary of {size} tokens and decode each predicted token into {control command}.

**Verify in primary sources:**

- `wang2025-vq-vla-improving-vision` — [VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.html) (ICCV 2025)
- `chen2025-moto-latent-motion-token` — [Moto: Latent Motion Token as the Bridging Language for Learning Robot Manipulation from Videos](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Moto_Latent_Motion_Token_as_the_Bridging_Language_for_Learning_ICCV_2025_paper.html) (ICCV 2025)

Catalog routes:
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/vision_language_action.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [topic: action_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/action_representation.md)
