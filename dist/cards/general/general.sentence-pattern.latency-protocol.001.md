# Super Library card: general.sentence-pattern.latency-protocol.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### Latency is measured on {hardware} with {precision, batch, and timing boundary}.

`general.sentence-pattern.latency-protocol.001` · sentence_pattern · general, robot_learning, vision_language_action · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Defines the hardware and measurement boundary required to interpret latency.

**Use:** State warm-up, synchronization, repeats, input shape, preprocessing, action decoding, and whether the value is model-only or end to end.

**Avoid:** Do not compare latency across hardware or confuse batched throughput with single-sample latency.

**Patterns:**

- Latency is measured on {hardware} at {precision} and batch size {value}, including {timing boundary}.
- End-to-end control latency includes {components} and is averaged over {repetitions} after {warm-up}.

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/general.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/vision_language_action.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
