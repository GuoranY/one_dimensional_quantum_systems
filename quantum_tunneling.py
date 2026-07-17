import numpy as np
import matplotlib.pyplot as plt
from quantum_utils import (
    transmission_probability
)


hbar = 1.0
mass = 1.0

barrier_height = 10.0
barrier_width = 1.0


energies = np.linspace(
    0.1,
    20.0,
    1000
)


# Calculate transmission probability

transmission = transmission_probability(
    energy=energies,
    barrier_height=barrier_height,
    barrier_width=barrier_width,
    hbar=hbar,
    mass=mass
)


# Plot the result

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    energies,
    transmission,
    label="Transmission probability"
)

plt.axvline(
    barrier_height,
    linestyle="--",
    label=rf"Barrier height $V_0={barrier_height}$"
)

plt.xlabel("Particle energy")
plt.ylabel("Transmission probability")
plt.title(
    "Quantum Tunneling Through a Rectangular Barrier"
)

plt.ylim(
    0,
    1.05
)

plt.grid(
    alpha=0.3
)

plt.legend()
plt.tight_layout()

plt.savefig(
    "figures/tunneling_transmission_vs_energy.png",
    dpi=300
)

plt.show()