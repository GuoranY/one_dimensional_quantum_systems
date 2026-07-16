import numpy as np
import matplotlib.pyplot as plt

from quantum_utils import (
    solve_schrodinger,
    find_bound_states
)


# Physical parameters

hbar = 1.0
mass = 1.0
barrier_energy = 20.0


# Numerical grid

num_points = 800
x = np.linspace(-3.0, 3.0, num_points)


# Well widths to investigate

well_width_values = [
    0.5,
    0.75,
    1.0,
    1.25,
    1.5,
    2.0
]

bound_state_counts = []


# Calculate the number of bound states for each well width

for well_width in well_width_values:

    # Finite square well potential:
    # V(x) = 0 inside the well
    # V(x) = barrier_energy outside the well

    potential = np.where(
        np.abs(x) <= well_width / 2,
        0.0,
        barrier_energy
    )

    energies, wavefunctions = solve_schrodinger(
        x=x,
        potential=potential,
        hbar=hbar,
        mass=mass
    )

    bound_energies, bound_wavefunctions = find_bound_states(
        energies=energies,
        wavefunctions=wavefunctions,
        barrier_energy=barrier_energy
    )

    number_of_bound_states = len(bound_energies)

    bound_state_counts.append(
        number_of_bound_states
    )

    print(
        f"Well width = {well_width:.2f}: "
        f"{number_of_bound_states} bound states"
    )


# Plot the number of bound states against well width

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    well_width_values,
    bound_state_counts,
    marker="o"
)

plt.xlabel(
    "Well Width"
)

plt.ylabel(
    "Number of Bound States"
)

plt.title(
    "Number of Bound States vs Well Width"
)

plt.grid(
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    "figures/bound_states_vs_width.png",
    dpi=300
)

plt.show()