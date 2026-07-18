import numpy as np
import matplotlib.pyplot as plt

from quantum_utils import (
    calculate_transmission_probability
)

# Physical parameters

hbar = 1.0
mass = 1.0

barrier_height = 10.0
barrier_width = 1.0


# Incident energy values

energy_values = np.linspace(
    0.1,
    barrier_height - 0.1,
    300
)


# Calculate transmission probabilities

transmission_probabilities = (
    calculate_transmission_probability(
        energy=energy_values,
        barrier_height=barrier_height,
        barrier_width=barrier_width,
        hbar=hbar,
        mass=mass
    )
)


# Print selected results

selected_energies = np.array(
    [
        1.0,
        2.0,
        4.0,
        6.0,
        8.0,
        9.0
    ]
)

selected_transmissions = (
    calculate_transmission_probability(
        energy=selected_energies,
        barrier_height=barrier_height,
        barrier_width=barrier_width,
        hbar=hbar,
        mass=mass
    )
)

print(
    "Energy dependence of tunnelling probability:\n"
)

print(
    f"{'Energy':>10}"
    f"{'Transmission Probability':>28}"
)

for energy, transmission in zip(
    selected_energies,
    selected_transmissions
):
    print(
        f"{energy:10.2f}"
        f"{transmission:28.8f}"
    )


# Plot transmission probability against energy

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    energy_values,
    transmission_probabilities,
    linewidth=2
)

plt.xlabel(
    "Incident Energy $E$"
)

plt.ylabel(
    "Transmission Probability $T$"
)

plt.title(
    "Energy Dependence of Quantum Tunneling"
)

plt.xlim(
    0,
    barrier_height
)

plt.yscale(
    "log"
)

plt.ylim(
    1e-5,
    1
)

plt.grid(
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    "figures/tunneling_energy_dependence.png",
    dpi=300
)

plt.show()