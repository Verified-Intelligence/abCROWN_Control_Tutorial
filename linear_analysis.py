import torch
import torch.nn as nn
from collections import defaultdict

from auto_LiRPA import BoundedModule, BoundedTensor, PerturbationLpNorm
from computation_graph import VanDerPolDynamics, Controller
from computation_graph import ClosedLoopComputationGraph


if __name__ == "__main__":
    # Linear analysis of x_dot = f(x, u(x))
    # We compute the linear bounds of the output layer w.r.t. the input layer

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
    lirpa_model = BoundedModule(close_loop_dynamics, (bounded_x,), device=device)

    # Step 4: Compute bounds using LiRPA
    # There are many bound coefficients during CROWN bound calculation, here we are interested in the linear bounds
    # of the output layer, with respect to the input layer (the state x).
    required_A = defaultdict(set)
    required_A[lirpa_model.output_name[0]].add(lirpa_model.input_name[0])

    lb, ub, A_dict = lirpa_model.compute_bounds(x=(bounded_x,), method="crown",
                                                return_A=True, needed_A_dict=required_A)
    lower_A = A_dict[lirpa_model.output_name[0]][lirpa_model.input_name[0]]['lA']
    lower_bias = A_dict[lirpa_model.output_name[0]][lirpa_model.input_name[0]]['lbias']
    upper_A = A_dict[lirpa_model.output_name[0]][lirpa_model.input_name[0]]['uA']
    upper_bias = A_dict[lirpa_model.output_name[0]][lirpa_model.input_name[0]]['ubias']
    print(f'lower bound linear coefficients size (batch, output_dim, *input_dims): {list(lower_A.size())}')
    print(f'upper bound linear coefficients size (batch, output_dim, *input_dims): {list(upper_A.size())}')
    print(f'lower bound linear bias size (batch, output_dim): {list(lower_bias.size())}')
    print(f'upper bound linear bias size (batch, output_dim): {list(upper_bias.size())}')
