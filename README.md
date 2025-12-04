# alpha-beta-CROWN Control Tutorial

## Overview

This tutorial provides step-by-step guidance and examples for using auto_LiRPA and alpha-beta-CROWN in control research..

## auto_LiRPA tutorial
We demonstrate three control-related applications using auto_LiRPA. The control system used in these examples is a simplified version of the Van der Pol system from our paper: [Two-Stage Learning of Stabilizing Neural Controllers via Zubov Sampling and Iterative Domain Expansion](https://arxiv.org/abs/2506.01356).

## Scripts
- ```bound_computation.py```: Builds a computation graph with the dynamical system and controller, and uses auto_LiRPA to directly compute bounds on the dynamics x_dot = f(x, u(x)).

- ```linear_analysis.py```: Shows how to extract linear relaxations, including both coefficients and biases, from any computation graph using auto_LiRPA.

- ```jacobian_bound.py```: Demonstrates how to compute bounds on a computation graph that includes Jacobian computations. In particular, it computes bounds for V_dot = grad(V) * f(x, u(x)), where V is the Lyapunov function of the system.

## alpha-beta-CROWN Demo
See the [Google Colab Demo](https://colab.research.google.com/drive/150LrqbN69WQejq4vK90iIX3QohNc8Ja3?usp=sharing#scrollTo=7Ydr7V7_iBQ3) for a step-by-step demonstration of verifying an image classification problem, a Lyapunov stability problem, and a discrete robot reachability problem.