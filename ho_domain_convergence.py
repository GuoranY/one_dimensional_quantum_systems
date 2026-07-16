import numpy as np
import matplotlib.pyplot as plt

from quantum_utils import solve_schrodinger


# Physical parameters in natural units

hbar = 1.0
mass = 1.0
omega = 1.0


# Half-widths of the computational domains:
# [-3, 3], [-4, 4], ..., [-10, 10]

domain_half_widths = [
    3.0,
    4.0,
    5.0,
    6.0,
    8.0,
    10.0
]


# Keep the grid spacing approximately fixed

target_dx = 0.02


# Number of low-energy states to compare

number_of_states = 5


# Analytical harmonic oscillator energies:
# E_n = hbar * omega * (n + 1/2)

quantum_numbers = np.arange(
    number_of_states
)

analytical_energies = (
    hbar
    * omega
    * (quantum_numbers + 0.5)
)


# Store results

numerical_energies = np.zeros(
    (
        len(domain_half_widths),
        number_of_states
    )
)

relative_errors = np.zeros_like(
    numerical_energies
)

actual_dx_values = []


# Solve the Schrodinger equation
# for each computational domain

for domain_index, half_width in enumerate(
    domain_half_widths
):

    x_min = -half_width
    x_max = half_width

    num_points = int(
        (x_max - x_min) / target_dx
    ) + 1

    x = np.linspace(
        x_min,
        x_max,
        num_points
    )

    actual_dx = x[1] - x[0]

    actual_dx_values.append(
        actual_dx
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

    numerical_energies[domain_index] = energies

    relative_errors[domain_index] = (
        np.abs(
            energies - analytical_energies
        )
        / analytical_energies
    )


# Print the convergence table

print(
    "Harmonic oscillator domain convergence\n"
)

header = (
    f"{'Half Width':>12}"
    f"{'Grid Points':>14}"
    f"{'dx':>12}"
)

for state_index in range(
    number_of_states
):
    header += (
        f"{f'E_{state_index} Error':>16}"
    )

print(header)


for domain_index, half_width in enumerate(
    domain_half_widths
):

    x_min = -half_width
    x_max = half_width

    num_points = int(
        (x_max - x_min) / target_dx
    ) + 1

    row = (
        f"{half_width:>12.1f}"
        f"{num_points:>14d}"
        f"{actual_dx_values[domain_index]:>12.6f}"
    )

    for state_index in range(
        number_of_states
    ):
        row += (
            f"{relative_errors[domain_index, state_index]:>16.3e}"
        )

    print(row)


# Plot relative error against domain half-width

plt.figure(
    figsize=(8, 6)
)

for state_index in range(
    number_of_states
):

    plt.semilogy(
        domain_half_widths,
        relative_errors[:, state_index],
        marker="o",
        label=f"n = {state_index}"
    )

plt.xlabel(
    "Domain Half-Width"
)

plt.ylabel(
    "Relative Energy Error"
)

plt.title(
    "Harmonic Oscillator Domain Convergence"
)

plt.grid(
    True,
    which="both",
    alpha=0.3
)

plt.legend()

plt.tight_layout()

plt.savefig(
    "figures/ho_domain_convergence.png",
    dpi=300
)

plt.show()