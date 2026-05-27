# α,β-CROWN Control Tutorial

This repo is the official repo for the ACC 2026 tutorial: [Bridging Control with Neural Network Verifier alpha-beta-CROWN:
A Tutorial](https://arxiv.org/pdf/2605.26577). This repository contains a standalone control tutorial notebook and the assets it needs:

- `control_tutorial.ipynb`
- `figures/`
- `neural_lyapunov_dependency/pendulum_discrete_state_feedback_quadratic.pt`

It provides code examples for various applications of α,β-CROWN in control problems, including reachability analysis, Lyapunov stability verification, and optimizing an MPC objective.

## 1) Install α,β-CROWN first

The notebook imports `abcrown` directly, so install abcrown before running the notebook, following the command below.

### Install from source

```bash
git clone --recursive https://github.com/Verified-Intelligence/alpha-beta-CROWN.git
cd alpha-beta-CROWN
# Create and activate a Python environment (example with conda):
conda create -n abcrown python=3.11 -y
conda activate abcrown
pip install -e .
pip install matplotlib
```

## Notes

- Paths in the notebook are relative to this repository root.
- The included checkpoint and figures are already placed in the expected locations.
