import numpy as np

from quantum_utils import (
    solve_schrodinger
)

hbar = 1.0
mass = 1.0

number_of_states = 5

x_min = 0.0
x_max = 1.0
num_points = 500

x = np.linspace(x_min, x_max, num_points)

x_interior = x[1:-1]

potential_interior = np.zeros_like(x_interior)

energies, wavefunctions_interior = solve_schrodinger(
    x=x_interior,
    potential=potential_interior,
    hbar=hbar,
    mass=mass,
    number_of_states=number_of_states
)

L = x_max - x_min

quantum_numbers = np.arange(
    1,
    number_of_states + 1
)

analytical_energies = (
    quantum_numbers**2
    * np.pi**2
    * hbar**2
    / (2 * mass * L**2)
)

relative_errors = (
    np.abs(energies - analytical_energies)
    / analytical_energies
)

print("Infinite square well energy comparison:\n")

for state_index in range(number_of_states):
    n = state_index + 1

    print(
        f"n = {n}: "
        f"numerical = {energies[state_index]:.8f}, "
        f"analytical = {analytical_energies[state_index]:.8f}, "
        f"relative error = {relative_errors[state_index]:.2e}"
    )

import matplotlib.pyplot as plt

plt.plot(
    quantum_numbers,
    relative_errors,
    "o-"
)

plt.xlabel("Quantum Number n")
plt.ylabel("Relative Error")
plt.title("Infinite Square Well Energy Errors")
plt.grid()

plt.savefig(
    "figures/infinite_well_energy_errors.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()