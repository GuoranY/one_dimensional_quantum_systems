import numpy as np
import matplotlib.pyplot as plt

from quantum_utils import (
    solve_schrodinger,
    find_bound_states
)


# Finite square well parameters

hbar = 1
mass = 1
L = 1

num_points = 800
x = np.linspace(-2, 2, num_points)

V0_values = [5, 10, 20, 40, 80]

bound_state_counts = []


# Calculate the number of bound states for each barrier height

for V0 in V0_values:

    # Finite square well potential:
    # V(x) = 0 inside the well
    # V(x) = V0 outside the well

    potential = np.where(
        np.abs(x) <= L / 2,
        0,
        V0
    )

    energies, wavefunctions = solve_schrodinger(
        x,
        potential,
        hbar=hbar,
        mass=mass
    )

    bound_energies, bound_wavefunctions = find_bound_states(
        energies,
        wavefunctions,
        V0
    )

    number_of_bound_states = len(bound_energies)

    bound_state_counts.append(number_of_bound_states)

    print(
        f"V0 = {V0:4}, "
        f"number of bound states = {number_of_bound_states}"
    )


# Plot the number of bound states against barrier height

plt.figure()

plt.step(
    V0_values,
    bound_state_counts,
    where="mid"
)

plt.plot(
    V0_values,
    bound_state_counts,
    "o"
)

plt.xlabel(r"Barrier Height $V_0$")
plt.ylabel("Number of Bound States")
plt.title("Number of Bound States vs Barrier Height")

plt.xticks(V0_values)

plt.yticks(
    range(
        min(bound_state_counts),
        max(bound_state_counts) + 1
    )
)

plt.grid()

plt.savefig(
    "figures/bound_states_vs_depth.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()