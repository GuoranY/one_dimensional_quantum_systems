import numpy as np
import matplotlib.pyplot as plt

from quantum_utils import (
    solve_schrodinger,
    probability_density
)


# Infinite square well parameters

L = 1.0
hbar = 1.0
mass = 1.0

number_of_grid_points = 500
number_of_states = 3

x = np.linspace(0, L, number_of_grid_points)


# The infinite square well requires:
# psi(0) = psi(L) = 0
#
# Therefore, solve the Schrödinger equation only on the
# interior grid points.

x_interior = x[1:-1]

potential_interior = np.zeros_like(x_interior)


# Solve the time-independent Schrödinger equation

energies, wavefunctions_interior = solve_schrodinger(
    x=x_interior,
    potential=potential_interior,
    hbar=hbar,
    mass=mass,
    number_of_states=number_of_states
)


# Add the boundary values psi(0) = psi(L) = 0

wavefunctions = np.zeros(
    (number_of_grid_points, number_of_states)
)

wavefunctions[1:-1, :] = wavefunctions_interior


# The overall sign of an eigenfunction is arbitrary.
# Flip each wavefunction so that it begins in the positive direction.

for state_index in range(number_of_states):
    if wavefunctions[1, state_index] < 0:
        wavefunctions[:, state_index] *= -1


# Compare numerical and analytical energies

n_values = np.arange(1, number_of_states + 1)

analytical_energies = (
    n_values**2
    * np.pi**2
    * hbar**2
    / (2 * mass * L**2)
)

print("Infinite square well energy comparison:\n")

for state_index, n in enumerate(n_values):
    numerical_energy = energies[state_index]
    analytical_energy = analytical_energies[state_index]

    relative_error = (
        abs(numerical_energy - analytical_energy)
        / analytical_energy
    )

    print(
        f"n = {n}: "
        f"numerical = {numerical_energy:.8f}, "
        f"analytical = {analytical_energy:.8f}, "
        f"relative error = {relative_error:.2e}"
    )


# Plot the numerical wavefunctions

plt.figure()

for state_index, n in enumerate(n_values):
    psi = wavefunctions[:, state_index]

    plt.plot(
        x,
        psi,
        label=f"n = {n}"
    )

plt.xlabel("x")
plt.ylabel(r"$\psi_n(x)$")
plt.title("Infinite Square Well Wavefunctions")
plt.grid()
plt.legend()

plt.savefig(
    "figures/infinite_well_wavefunctions.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Plot the probability densities

plt.figure()

for state_index, n in enumerate(n_values):
    psi = wavefunctions[:, state_index]

    probability = probability_density(psi)

    plt.plot(
        x,
        probability,
        label=f"n = {n}"
    )

plt.xlabel("x")
plt.ylabel(r"$|\psi_n(x)|^2$")
plt.title("Infinite Square Well Probability Densities")
plt.grid()
plt.legend()

plt.savefig(
    "figures/infinite_well_probability_density.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Plot the numerical energy levels

plt.figure()

for state_index, n in enumerate(n_values):
    energy = energies[state_index]

    plt.hlines(
        energy,
        xmin=0,
        xmax=1
    )

    plt.text(
        1.03,
        energy,
        f"n = {n}, E = {energy:.3f}",
        va="center",
        fontsize=9
    )

plt.xlim(0, 1.4)
plt.xlabel("State")
plt.ylabel(r"$E_n$ (natural units)")
plt.title("Infinite Square Well Energy Levels")
plt.grid(axis="y")

plt.savefig(
    "figures/infinite_well_energy_levels.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()