# Super Library card: emb.term.grasp-pose.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### 6-DoF grasp pose

`emb.term.grasp-pose.001` · term · robot_learning · introduction, related_work, method, experiments, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A candidate gripper pose in three-dimensional space parameterized by three translational and three rotational degrees of freedom.

**Use:** Define the coordinate frame, gripper model, collision checks, and evaluation criterion. Separate pose proposal quality from executed grasp success.

**Avoid:** Do not call an image-plane grasp rectangle a full 6-DoF grasp pose.

**Patterns:**

- The network predicts 6-DoF grasp poses from {RGB-D image or point cloud}.
- We transform each grasp pose from {camera frame} to {robot base frame}.

**Verify in primary sources:**

- `fang2020graspnet` — [GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping](https://openaccess.thecvf.com/content_CVPR_2020/html/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.html) (CVPR 2020)

Catalog routes:
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/robot_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/experiments.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: robot_manipulation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/robot_manipulation.md)
