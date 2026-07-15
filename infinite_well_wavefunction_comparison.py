import numpy as np
import matplotlib.pyplot as plt

from quantum_utils import solve_schrodinger


# Parameters

hbar = 1.0
mass = 1.0
L = 1.0

number_of_states = 3
num_points = 500

x = np.linspace(0.0, L, num_points)

# The infinite-well boundary conditions are:
# psi(0) = psi(L) = 0

x_interior = x[1:-1]
potential_interior = np.zeros_like(x_interior)


# Numerical solution

energies, wavefunctions_interior = solve_schrodinger(
    x=x_interior,
    potential=potential_interior,
    hbar=hbar,
    mass=mass,
    number_of_states=number_of_states
)


# Compare numerical and analytical wavefunctions

for state_index in range(number_of_states):
    n = state_index + 1

    analytical_wavefunction = (
        np.sqrt(2.0 / L)
        * np.sin(n * np.pi * x / L)
    )

    # Add the zero-valued boundary points to the numerical solution
    numerical_wavefunction = np.zeros_like(x)

    numerical_wavefunction[1:-1] = (
        wavefunctions_interior[:, state_index]
    )

    # Eigenvectors may differ by an overall sign.
    # Reverse the numerical wavefunction when necessary.
    overlap = np.trapezoid(
        analytical_wavefunction * numerical_wavefunction,
        x
    )

    if overlap < 0:
        numerical_wavefunction *= -1

    plt.plot(
        x,
        analytical_wavefunction,
        label=f"Analytical, n = {n}"
    )

    plt.plot(
        x,
        numerical_wavefunction,
        linestyle="--",
        label=f"Numerical, n = {n}"
    )


plt.xlabel("x")
plt.ylabel(r"$\psi_n(x)$")
plt.title("Infinite Square Well Wavefunction Comparison")
plt.grid()
plt.legend()

plt.savefig(
    "figures/infinite_well_wavefunction_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()