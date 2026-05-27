# α,β-CROWN Control Tutorial

This repo accompanies the ACC 2026 tutorial: [Bridging Control with Neural Network Verifier alpha-beta-CROWN:
A Tutorial](https://arxiv.org/pdf/2605.26577). This repository contains a standalone control tutorial notebook and the assets it needs:

- `control_tutorial.ipynb`
- `figures/`
- `neural_lyapunov_dependency/pendulum_discrete_state_feedback_quadratic.pt`

It provides code examples to demonstrate various applications of α,β-CROWN in control problems, including reachability analysis, Lyapunov stability verification, and optimizing an MPC objective.

## 1. Install α,β-CROWN

The notebook imports `abcrown` directly, so install abcrown before running the notebook, following the command below.

```bash
git clone --recursive https://github.com/Verified-Intelligence/alpha-beta-CROWN.git
cd alpha-beta-CROWN
# Create and activate a Python environment (example with conda):
conda create -n abcrown python=3.11 -y
conda activate abcrown
pip install -e .
pip install matplotlib
```

## 2. Run the Tutorial Notebook

Simply open and run

```bash
control_tutorial.ipynb
```

## Notes

- The notebook is designed to be self-contained once α,β-CROWN is installed.
- Paths in the notebook are relative to this repository root, and the included checkpoint and figures are already placed in the expected locations.
