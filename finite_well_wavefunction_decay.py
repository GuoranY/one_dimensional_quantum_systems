import numpy as np
import matplotlib.pyplot as plt

from quantum_utils import (
    solve_schrodinger,
    find_bound_states
)


# Physical parameters

hbar = 1.0
mass = 1.0

well_width = 1.0
barrier_energy = 20.0


# Numerical grid

# The computational region is wider than the plotted region
# so that the artificial boundaries do not appear in the plots.

x_min = -5.0
x_max = 5.0
num_points = 2000

x = np.linspace(
    x_min,
    x_max,
    num_points
)


# Finite square well potential

potential = np.where(
    np.abs(x) <= well_width / 2,
    0.0,
    barrier_energy
)


# Solve the Schrodinger equation

energies, wavefunctions = solve_schrodinger(
    x=x,
    potential=potential,
    hbar=hbar,
    mass=mass
)


# Select bound states

bound_energies, bound_wavefunctions = find_bound_states(
    energies=energies,
    wavefunctions=wavefunctions,
    barrier_energy=barrier_energy
)

if len(bound_energies) == 0:
    raise RuntimeError(
        "No bound states were found."
    )


# Select the ground state

state_index = 0

energy = bound_energies[state_index]

wavefunction = (
    bound_wavefunctions[:, state_index].copy()
)


# Fix the arbitrary sign of the eigenvector

largest_amplitude_index = np.argmax(
    np.abs(wavefunction)
)

if wavefunction[largest_amplitude_index] < 0:
    wavefunction = -wavefunction


# Theoretical decay constant

# For E < V0, the wavefunction outside the well
# behaves approximately as exp(-kappa x).

kappa_theoretical = np.sqrt(
    2.0
    * mass
    * (barrier_energy - energy)
) / hbar


print(
    f"Ground-state energy: "
    f"{energy:.6f}"
)

print(
    f"Theoretical decay constant: "
    f"{kappa_theoretical:.6f}"
)


# Plot 1: Ground-state wavefunction

plt.figure(figsize=(8, 5))

plt.plot(
    x,
    wavefunction,
    label=fr"Ground state, $E={energy:.4f}$"
)

plt.axvline(
    -well_width / 2,
    linestyle="--",
    label="Well boundaries"
)

plt.axvline(
    well_width / 2,
    linestyle="--"
)

plt.axhline(
    0.0,
    linewidth=0.8
)

# The numerical boundaries are at x = -5 and x = 5,
# but only the central region is displayed.

plt.xlim(-3.0, 3.0)

plt.xlabel("x")
plt.ylabel(r"$\psi(x)$")

plt.title(
    "Finite Square Well Ground-State Wavefunction"
)

plt.grid()
plt.legend()

plt.savefig(
    "figures/finite_well_wavefunction_decay.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Plot 2: Wavefunction magnitude on a logarithmic scale

# Prevent zero or extremely small numerical values
# from causing problems on the logarithmic axis.

wavefunction_magnitude = np.maximum(
    np.abs(wavefunction),
    1e-14
)

plt.figure(figsize=(8, 5))

plt.semilogy(
    x,
    wavefunction_magnitude,
    label=r"$|\psi(x)|$"
)

plt.axvline(
    -well_width / 2,
    linestyle="--",
    label="Well boundaries"
)

plt.axvline(
    well_width / 2,
    linestyle="--"
)

plt.xlim(-3.0, 3.0)

plt.xlabel("x")
plt.ylabel(r"$|\psi(x)|$")

plt.title(
    "Exponential Decay Outside the Finite Square Well"
)

plt.grid()
plt.legend()

plt.savefig(
    "figures/finite_well_wavefunction_decay_log.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()