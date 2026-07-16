import numpy as np
import matplotlib.pyplot as plt

from quantum_utils import solve_schrodinger


# Physical parameters in natural units

hbar = 1.0
mass = 1.0
omega = 1.0


# Fixed computational domain

x_min = -8.0
x_max = 8.0


# Grid sizes used in the convergence study

num_points_values = [
    100,
    200,
    400,
    800,
    1200
]


# Number of low-energy states to compare

number_of_states = 5


# Analytical harmonic oscillator energies:
# E_n = hbar * omega * (n + 1/2)

quantum_numbers = np.arange(number_of_states)

analytical_energies = (
    hbar
    * omega
    * (quantum_numbers + 0.5)
)


# Store numerical results

numerical_energies = np.zeros(
    (
        len(num_points_values),
        number_of_states
    )
)

relative_errors = np.zeros_like(
    numerical_energies
)


# Solve the Schrodinger equation for each grid size

for grid_index, num_points in enumerate(
    num_points_values
):

    x = np.linspace(
        x_min,
        x_max,
        num_points
    )

    potential = (
        0.5
        * mass
        * omega**2
        * x**2
    )

    energies, wavefunctions = solve_schrodinger(
        x=x,
        potential=potential,
        hbar=hbar,
        mass=mass,
        number_of_states=number_of_states
    )

    numerical_energies[grid_index] = energies

    relative_errors[grid_index] = (
        np.abs(
            energies - analytical_energies
        )
        / analytical_energies
    )


# Print an energy comparison table

print(
    "Harmonic oscillator grid convergence\n"
)

header = (
    f"{'Grid Points':>12}"
    f"{'dx':>12}"
)

for state_index in range(number_of_states):
    header += (
        f"{f'E_{state_index} Error':>16}"
    )

print(header)

for grid_index, num_points in enumerate(
    num_points_values
):

    dx = (
        x_max - x_min
    ) / (
        num_points - 1
    )

    row = (
        f"{num_points:>12d}"
        f"{dx:>12.6f}"
    )

    for state_index in range(number_of_states):
        row += (
            f"{relative_errors[grid_index, state_index]:>16.3e}"
        )

    print(row)


# Plot relative error against grid size

plt.figure(
    figsize=(8, 6)
)

for state_index in range(number_of_states):

    plt.loglog(
        num_points_values,
        relative_errors[:, state_index],
        marker="o",
        label=f"n = {state_index}"
    )

plt.xlabel(
    "Number of Grid Points"
)

plt.ylabel(
    "Relative Energy Error"
)

plt.title(
    "Harmonic Oscillator Grid Convergence"
)

plt.grid(
    True,
    which="both",
    alpha=0.3
)

plt.legend()

plt.tight_layout()

plt.savefig(
    "figures/ho_grid_convergence.png",
    dpi=300
)

plt.show()