# Super Library card: vla.term.embodiment-specific-decoder.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### embodiment-specific action decoder

`vla.term.embodiment-specific-decoder.001` · term · vision_language_action, robot_learning · method, related_work

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A decoder specialized to the action space or control interface of one robot embodiment while upstream representations may be shared.

**Use:** Name the shared representation, embodiment identifier, action dimensions, and which decoder parameters remain robot-specific.

**Avoid:** Do not claim cross-embodiment transfer from a shared backbone alone; establish what transfers and what is retrained.

**Patterns:**

- We share {representation} across robots and use an embodiment-specific decoder for {action space}.

**Verify in primary sources:**

- `yuan2025-cross-embodiment-dexterous-grasping` — [Cross-Embodiment Dexterous Grasping with Reinforcement Learning](https://iclr.cc/virtual/2025/poster/28010) (ICLR 2025)
- `miao2025-fedvla-federated-vision-language` — [FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation](https://openaccess.thecvf.com/content/ICCV2025/html/Miao_FedVLA_Federated_Vision-Language-Action_Learning_with_Dual_Gating_Mixture-of-Experts_for_Robotic_ICCV_2025_paper.html) (ICCV 2025)

Catalog routes:
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/vision_language_action.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/robot_learning.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [topic: robot_foundation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/robot_foundation.md)
- [topic: action_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/action_representation.md)
