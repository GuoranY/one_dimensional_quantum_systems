import numpy as np
import matplotlib.pyplot as plt

from quantum_utils import (
    calculate_transmission_probability
)


# Physical parameters

hbar = 1.0
mass = 1.0

energy = 2.0
barrier_width = 1.0


# Barrier height values

barrier_height_values = np.linspace(
    energy + 0.1,
    20.0,
    300
)


# Calculate transmission probabilities

transmission_probabilities = []

for barrier_height in barrier_height_values:

    transmission = (
        calculate_transmission_probability(
            energy=np.array([energy]),
            barrier_height=barrier_height,
            barrier_width=barrier_width,
            hbar=hbar,
            mass=mass
        )
    )

    transmission_probabilities.append(
        transmission[0]
    )

transmission_probabilities = np.array(
    transmission_probabilities
)


# Print selected results

selected_barrier_heights = [
    3.0,
    5.0,
    8.0,
    10.0,
    15.0,
    20.0
]

print(
    "Barrier-height dependence of tunnelling probability:\n"
)

print(
    f"{'Barrier Height':>16}"
    f"{'Transmission Probability':>28}"
)

for barrier_height in selected_barrier_heights:

    transmission = (
        calculate_transmission_probability(
            energy=np.array([energy]),
            barrier_height=barrier_height,
            barrier_width=barrier_width,
            hbar=hbar,
            mass=mass
        )
    )[0]

    print(
        f"{barrier_height:16.2f}"
        f"{transmission:28.8e}"
    )


# Plot transmission probability against barrier height

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    barrier_height_values,
    transmission_probabilities,
    linewidth=2
)

plt.xlabel(
    "Barrier Height $V_0$"
)

plt.ylabel(
    "Transmission Probability $T$"
)

plt.title(
    "Barrier-Height Dependence of Quantum Tunneling"
)

plt.yscale(
    "log"
)

plt.xlim(
    energy,
    20.0
)

plt.grid(
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    "figures/tunneling_height_dependence.png",
    dpi=300
)

plt.show()