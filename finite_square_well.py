import numpy as np
import matplotlib.pyplot as plt

from quantum_utils import (
    solve_schrodinger,
    find_bound_states
)


# Finite square well parameters

L = 1
V0 = 20
hbar = 1
mass = 1

x = np.linspace(-2, 2, 1000)


# Potential:
# V(x) = 0 inside the well
# V(x) = V0 outside the well

V = np.where(
    np.abs(x) <= L / 2,
    0,
    V0
)


# Plot the potential

plt.figure()
plt.plot(x, V)

plt.xlabel("x")
plt.ylabel("V(x)")
plt.title("Finite Square Well Potential")
plt.ylim(-2, V0 + 5)
plt.grid()

plt.savefig(
    "figures/finite_well_potential.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Solve the Schrodinger equation

energies, wavefunctions = solve_schrodinger(
    x=x,
    potential=V,
    hbar=hbar,
    mass=mass
)

print("First five numerical energy eigenvalues:")
print(energies[:5])


# Identify bound states

bound_energies, bound_wavefunctions = find_bound_states(
    energies=energies,
    wavefunctions=wavefunctions,
    barrier_energy=V0
)

print("Bound-state energies:")
print(bound_energies)

print(
    f"Number of bound states: {len(bound_energies)}"
)


# Plot bound-state wavefunctions

for state_index, energy in enumerate(bound_energies):
    psi = bound_wavefunctions[:, state_index]

    plt.plot(
        x,
        psi,
        label=f"E = {energy:.2f}"
    )

plt.xlabel("x")
plt.ylabel(r"$\psi(x)$")
plt.title("Bound States in a Finite Square Well")
plt.grid()
plt.legend()

plt.savefig(
    "figures/finite_well_wavefunctions.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Plot potential, energy levels, and shifted wavefunctions

plt.plot(
    x,
    V,
    label="Potential V(x)"
)

wavefunction_scale = 2.0

for state_index, energy in enumerate(bound_energies):
    psi = bound_wavefunctions[:, state_index]

    # Shift the wavefunction upward to its energy level
    shifted_psi = (
        energy
        + wavefunction_scale * psi
    )

    plt.plot(
        x,
        shifted_psi,
        label=f"State at E = {energy:.2f}"
    )

    # Draw the corresponding energy level
    plt.hlines(
        energy,
        xmin=x[0],
        xmax=x[-1],
        linestyles="dashed"
    )

plt.xlabel("x")
plt.ylabel("Energy")
plt.title("Finite Square Well Bound States")
plt.ylim(-2, V0 + 5)
plt.grid()
plt.legend()

plt.savefig(
    "figures/finite_well_bound_states.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()