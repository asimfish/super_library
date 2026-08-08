# Super Library card: vla.definition.chain-of-affordance.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### chain-of-affordance reasoning

`vla.definition.chain-of-affordance.001` · definition · vision_language_action, embodied_ai · related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

An intermediate reasoning formulation that decomposes a manipulation instruction into action-relevant object, spatial, or interaction affordances before control prediction.

**Use:** State the intermediate representation, its supervision, and whether it is generated explicitly at inference time.

**Avoid:** Do not treat an interpretable-looking intermediate output as causal evidence that the policy used the stated reasoning process.

**Patterns:**

- The model predicts {affordance representation} as an intermediate target before decoding {robot action}.

**Verify in primary sources:**

- `li2025-coa-vla-improving-vision` — [CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance](https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html) (ICCV 2025)
- `zhao2025-cot-vla-visual-chain` — [CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html) (CVPR 2025)

Catalog routes:
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/vision_language_action.md)
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [topic: vla_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/vla_models.md)
- [topic: robot_manipulation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/robot_manipulation.md)
