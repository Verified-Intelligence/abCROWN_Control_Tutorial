# α,β-CROWN Control Tutorial

This repo is the official repo for the ACC 2026 tutorial: [Bridging Control with Neural Network Verifier alpha-beta-CROWN:
A Tutorial](https://arxiv.org/pdf/2605.26577). This repository contains a standalone control tutorial notebook and the assets it needs:

- `control_tutorial.ipynb`
- `figures/`
- `neural_lyapunov_dependency/pendulum_discrete_state_feedback_quadratic.pt`

## 1) Install α,β-CROWN first

The notebook imports `abcrown` directly, so install abcrown before running the notebook.

### Option A: Install from an existing local alpha-beta-CROWN checkout

```bash
cd /path/to/alpha-beta-CROWN
# Create/activate your Python environment first (conda/venv).
pip install -e .
```

### Option B: Fresh install from source

```bash
git clone https://github.com/Verified-Intelligence/alpha-beta-CROWN.git
cd alpha-beta-CROWN
# Create and activate a Python environment (example with conda):
conda create -n abcrown python=3.11 -y
conda activate abcrown
pip install -e .
pip install matplotlib
```

If you need CUDA-specific PyTorch builds or extra dependencies, follow the official installation notes in the alpha-beta-CROWN repository first, then run `pip install -e .`.

## Notes

- Paths in the notebook are relative to this repository root.
- The included checkpoint and figures are already placed in the expected locations.
