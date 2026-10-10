# Research log

Newest entry first. For each session: what I read, what I tried, what failed, what's next.

---

## 2026-10-09: Research environment

- **Did:** new Python 3.12 environment with uv; installed RDKit, scikit-learn, XGBoost, scanpy, PyTorch, MONAI, nibabel, SimpleITK. `scripts/check_env.py` passes and the Apple GPU (MPS) works.
- **Failed:** XGBoost couldn't load at first because the OpenMP runtime was missing. Fixed with `brew install libomp`.
- **Next:** Kaggle + Colab accounts; anchor paper 2 (Filbin 2018).

## 2026-10-08: somatic histone H3 paper
- they found that out of about 43 - 50 DIPGs and 36 non-brainstem paediatric glioblastomas (non-BS-PGs). 78% of DIPGs and 22% of non-BS-PGs contained p.K27M mutation in H3F3A, encoding histone H3.3, or the related HISTIH3B, encoding histone H3.1.(i.e 78% of DIPGs had K27M in either H3F3A or HIST1H3B. that's the two genes combined, not H3F3A alone.) they also found that an additional 14% of non BS-PGs had somatic p.G34R H3F3A mutations.
- they found these by performing whole genome sequencing of 7 DIPGs and matched germline DNA, and targeted sequencing of an additional 43 DIPGs and 36 non-brainstem paediatric glioblastomas. trying to identify somatic mutations in paediatric diffuse intrinsic pontine gliomas(DIPGs).
- i didn't understand the acronyms.

#### acronyms from the paper:
- H3F3A is the gene that makes histone H3.3. HIST1H3B(Histone cluster 1, H3b) makes histone H3.1.
- p.K27M means the amino acid at position 27 changes from lysine (K) to methionine (M). That's "H3K27M".
- p.G34R means position 34 changes from glycine (G) to arginine (R).
- non-BS-PG stands for non-brainstem paediatric glioblastoma.

## 2026-10-07: Repo cleanup (Phase 0)

- **Did:** tagged the MEG work as `v1-meg`; untracked `.venv/` and raw data (`dataset/`); removed stray `=4.2.0` and `.c` files; added `.gitignore`; rewrote the README for v2.
- **Learned:** never commit virtual environments or raw data. Quote version specifiers in pip (`pip install "pkg>=4.2.0"`), or the shell writes a file named `=4.2.0`.
- **Next:** toolchain (RDKit, scikit-learn, scanpy, PyTorch MPS, MONAI); first anchor paper.
