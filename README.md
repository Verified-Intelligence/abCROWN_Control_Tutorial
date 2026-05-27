# α,β-CROWN Control Tutorial

This repository accompanies the ACC 2026 tutorial: [Bridging Control with Neural Network Verifier α,β-CROWN: A Tutorial](https://arxiv.org/pdf/2605.26577).

It provides a standalone tutorial notebook and the supporting assets needed to run the examples:

- `control_tutorial.ipynb`
- `figures/`
- `neural_lyapunov_dependency/pendulum_discrete_state_feedback_quadratic.pt`

The tutorial demonstrates several applications of α,β-CROWN to control problems, including reachability analysis, Lyapunov stability verification, and MPC objective optimization. Its goal is to show how α,β-CROWN can be used in control-oriented verification and optimization workflows, rather than to explain the underlying verification algorithms in detail.

For readers interested in the neural network verification algorithms behind α,β-CROWN, a more detailed tutorial is available at this [neural network verification tutorial](https://neural-network-verification.com/).

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
