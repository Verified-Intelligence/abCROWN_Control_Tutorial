import torch
import torch.nn as nn

from auto_LiRPA import BoundedModule, BoundedTensor, PerturbationLpNorm
from auto_LiRPA.jacobian import JacobianOP
from computation_graph import VanDerPolDynamics, Controller, Lyapunov


# Construct the computation graph for V_dot = ∇V · f(x, u(x))
class LyapunovDotComputationGraph(nn.Module):
    def __init__(self, dynamics: VanDerPolDynamics, controller: Controller, lyapunov: Lyapunov):
        super().__init__()
        self.dynamics = dynamics
        self.controller = controller
        self.lyapunov = lyapunov

    def forward(self, x):
        u = self.controller(x)
        x_dot = self.dynamics.f_torch(x, u)
        V_x = self.lyapunov(x)
        # Compute the Jacobian of V w.r.t. x using JacobianOP
        dVdx = JacobianOP.apply(V_x, x).squeeze(1)
        V_dot = torch.sum(dVdx * x_dot, dim=1, keepdim=True)
        return V_dot


if __name__ == "__main__":
    # Compute bounds for V_dot = ∇V · f(x, u(x))

    # Step 1: Define computation graph by implementing forward()
    dynamics = VanDerPolDynamics()
    controller = Controller(dims=[2, 10, 10, 1],
                            x_equilibrium=dynamics.x_equilibrium,
                            u_equilibrium=dynamics.u_equilibrium,
                            scale=1.0)
    lyapunov = Lyapunov(dims=[2, 40, 40, 1])

    lyapunov_dot_dynamics = LyapunovDotComputationGraph(dynamics, controller, lyapunov)
    # Now lyapunov_dot_dynamics is a nn.Module,
    # with input the state x, and output the time derivative of the Lyapunov function V_dot
    # NOTE: in the original Torch model, the operator JacobianOP is just a placeholder,
    # it does not actually compute the Jacobian.

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
    lirpa_model = BoundedModule(lyapunov_dot_dynamics, (bounded_x,), device=device)
    # NOTE: in the initialization of BoundedModule, the operator JacobianOP
    # is expanded into a series "gradient" operations and added to the computation graph.
    # So now lirpa_model contains the correct computation graph for V_dot.

    # Optional: visualize the computation graph
    # You can see how JacobianOP is expanded in the graph.
    lirpa_model.visualize("images/bounded_lyapunov_dot_dynamics")
    print()

    # Step 4: Compute bounds using LiRPA
    lb, ub = lirpa_model.compute_bounds(x=(bounded_x,), method="crown")
    # You can also use other methods, e.g., "IBP", "forward", "forward+backward", "alpha-crown" etc.
    print("Bounds for V_dot = ∇V · f(x, u(x)):")
    print("Lower bound:", lb)
    print("Upper bound:", ub)
