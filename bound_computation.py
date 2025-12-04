import torch
import torch.nn as nn

from auto_LiRPA import BoundedModule, BoundedTensor, PerturbationLpNorm
from computation_graph import VanDerPolDynamics, Controller
from computation_graph import ClosedLoopComputationGraph


if __name__ == "__main__":
    # Compute bounds for x_dot = f(x, u(x))

    # Step 1: Define computation graph by implementing forward()
    dynamics = VanDerPolDynamics()
    controller = Controller(dims=[2, 10, 10, 1],
                            x_equilibrium=dynamics.x_equilibrium,
                            u_equilibrium=dynamics.u_equilibrium,
                            scale=1.0)

    close_loop_dynamics = ClosedLoopComputationGraph(dynamics, controller)
    # Now close_loop_dynamics is a nn.Module,
    # with input the state x, and output the state derivative x_dot

    # TODO: load weights here

    # auto_LiRPA can use both CPU and GPU
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print('Running on', device)

    # Step 2: Define the input to be perturbed
    x_L = torch.tensor([[-1.0, -1.0]], device=device)
    x_U = torch.tensor([[1.0, 1.0]], device=device)
    ptb = PerturbationLpNorm(x_L=x_L, x_U=x_U)
    # Define the BoundedTensor as input
    bounded_x = BoundedTensor(torch.zeros(1, 2, device=device), ptb)

    # Step 3: Wrap the model with auto_LiRPA
    # The second parameter is for constructing the trace of the computational graph,
    # It's a tuple of all inputs (there can be multiple input nodes)
    # If all inputs are torch.Tensor, we assume that all inputs are perturbed.
    # If some inputs are BoundedTensor, we assume that only those inputs are perturbed.
    lirpa_model = BoundedModule(close_loop_dynamics, (bounded_x,), device=device)

    # Optional: visualize the computation graph
    # It's highly recommended to visualize the graph to make sure it's correct
    # (e.g., shape of each node, perturbed nodes, etc.)
    # Visualization file is saved as "bounded_closed_loop_dynamics.png" or "bounded_closed_loop_dynamics.dot"
    lirpa_model.visualize("images/bounded_closed_loop_dynamics")
    print()

    # Step 4: Compute bounds using LiRPA
    lb, ub = lirpa_model.compute_bounds(x=(bounded_x,), method="crown")
    # You can also use other methods, e.g., "IBP", "forward", "forward+backward", "alpha-crown" etc.
    print("Bounds for one step closed-loop dynamics:")
    print("Lower bound:", lb)
    print("Upper bound:", ub)
