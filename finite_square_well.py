import numpy as np
import matplotlib.pyplot as plt

# Finite square well parameters
L = 1
V0 = 20

x = np.linspace(-2, 2, 1000)

# Potential:
# V(x) = 0 inside the well
# V(x) = V0 outside the well
V = np.where(np.abs(x) <= L / 2, 0, V0)

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


# Finite-difference Hamiltonian

hbar = 1
m = 1

dx = x[1] - x[0]
N = len(x)

main_diagonal = np.full(
    N,
    hbar**2 / (m * dx**2)
) + V

off_diagonal = np.full(
    N - 1,
    -hbar**2 / (2 * m * dx**2)
)

H = (
    np.diag(main_diagonal)
    + np.diag(off_diagonal, 1)
    + np.diag(off_diagonal, -1)
)
energies, wavefunctions = np.linalg.eigh(H)

print(energies[:5])


# Identify bound states

bound_state_indices = np.where(energies < V0)[0]

print("Bound-state energies:")
print(energies[bound_state_indices])

# Plot bound-state wavefunctions
for index in bound_state_indices:
    psi = wavefunctions[:, index]

    # Normalize using numerical integration
    norm = np.sqrt(np.trapezoid(np.abs(psi) ** 2, x))
    psi = psi / norm

    plt.plot(
        x,
        psi,
        label=f"E = {energies[index]:.2f}"
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

plt.plot(x, V, label="Potential V(x)")

wavefunction_scale = 2.0

for index in bound_state_indices:
    energy = energies[index]
    psi = wavefunctions[:, index]

    # Normalize the wavefunction
    norm = np.sqrt(np.trapezoid(np.abs(psi) ** 2, x))
    psi = psi / norm

    # Shift the wavefunction upward to its energy level
    shifted_psi = energy + wavefunction_scale * psi

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