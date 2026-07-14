import numpy as np
import matplotlib.pyplot as plt

from quantum_utils import solve_schrodinger


hbar = 1.0
mass = 1.0

x_min = 0.0
x_max = 1.0

num_points_values = [
    50,
    100,
    200,
    400,
    800
]

numerical_energies = []

for num_points in num_points_values:
    x = np.linspace(
        x_min,
        x_max,
        num_points
    )

    x_interior = x[1:-1]

    potential_interior = np.zeros_like(
        x_interior
    )

    energies, _ = solve_schrodinger(
        x=x_interior,
        potential=potential_interior,
        hbar=hbar,
        mass=mass,
        number_of_states=1
    )

    numerical_energies.append(
        energies[0]
    )


L = x_max - x_min

analytical_energy = (
    np.pi**2
    * hbar**2
    / (2 * mass * L**2)
)

relative_errors = (
    np.abs(
        np.array(numerical_energies)
        - analytical_energy
    )
    / analytical_energy
)


plt.plot(
    num_points_values,
    relative_errors,
    marker="o"
)

plt.xlabel("Number of Grid Points")
plt.ylabel("Relative Error")
plt.yscale("log")
plt.title("Infinite Square Well Numerical Convergence")
plt.grid()

plt.savefig(
    "figures/infinite_well_convergence.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()