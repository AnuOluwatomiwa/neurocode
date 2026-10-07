# Research log

Newest entry first. For each session: what I read, what I tried, what failed, what's next.

---

## 2026-10-07: Repo cleanup (Phase 0)

- **Did:** tagged the MEG work as `v1-meg`; untracked `.venv/` and raw data (`dataset/`); removed stray `=4.2.0` and `.c` files; added `.gitignore`; rewrote the README for v2.
- **Learned:** never commit virtual environments or raw data. Quote version specifiers in pip (`pip install "pkg>=4.2.0"`), or the shell writes a file named `=4.2.0`.
- **Next:** toolchain (RDKit, scikit-learn, scanpy, PyTorch MPS, MONAI); first anchor paper.
