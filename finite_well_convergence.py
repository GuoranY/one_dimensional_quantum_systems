import numpy as np
import matplotlib.pyplot as plt

from quantum_utils import (
    solve_schrodinger,
    find_bound_states
)


# Physical parameters
HBAR = 1.0
MASS = 1.0
L = 1.0
V0 = 20.0

# Grid sizes used in the convergence test
NUM_POINTS_LIST = [65, 129, 257, 513, 1025]


def calculate_bound_energies(num_points):
    """
    Calculate the bound-state energies of a finite square well
    using a grid containing num_points points.
    """

    # Spatial grid
    x = np.linspace(-2, 2, num_points)

    # Finite square well potential:
    # V(x) = 0 inside the well
    # V(x) = V0 outside the well
    potential = np.where(
        np.abs(x) <= L / 2,
        0.0,
        V0
    )

    # Solve the time-independent Schrödinger equation
    energies, wavefunctions = solve_schrodinger(
        x,
        potential,
        hbar=HBAR,
        mass=MASS
    )

    # Select states whose energies are below the barrier height
    bound_energies, _ = find_bound_states(
        energies,
        wavefunctions,
        V0
    )

    return bound_energies


ground_state_energies = []
first_excited_energies = []


# Calculate energies for each grid size
for num_points in NUM_POINTS_LIST:
    bound_energies = calculate_bound_energies(num_points)

    # Make sure at least two bound states were found
    if len(bound_energies) < 2:
        raise RuntimeError(
            f"Only {len(bound_energies)} bound state(s) found "
            f"for N = {num_points}. At least two are required."
        )

    ground_state_energy = bound_energies[0]
    first_excited_energy = bound_energies[1]

    ground_state_energies.append(ground_state_energy)
    first_excited_energies.append(first_excited_energy)

    print(
        f"N = {num_points:4d}, "
        f"E0 = {ground_state_energy:.8f}, "
        f"E1 = {first_excited_energy:.8f}"
    )


# Calculate changes between consecutive grid sizes
delta_E0_list = []
delta_E1_list = []

print("\nChanges between consecutive grid sizes:")

for i in range(1, len(NUM_POINTS_LIST)):
    delta_E0 = abs(
        ground_state_energies[i]
        - ground_state_energies[i - 1]
    )

    delta_E1 = abs(
        first_excited_energies[i]
        - first_excited_energies[i - 1]
    )

    delta_E0_list.append(delta_E0)
    delta_E1_list.append(delta_E1)

    print(
        f"N = {NUM_POINTS_LIST[i]:4d}: "
        f"|ΔE0| = {delta_E0:.8f}, "
        f"|ΔE1| = {delta_E1:.8f}"
    )


# Plot convergence errors
plt.figure(figsize=(7, 5))

plt.plot(
    NUM_POINTS_LIST[1:],
    delta_E0_list,
    "o-",
    label="Ground state"
)

plt.plot(
    NUM_POINTS_LIST[1:],
    delta_E1_list,
    "o-",
    label="First excited state"
)

plt.xlabel("Grid size N")
plt.ylabel(r"$|E_N - E_{\mathrm{previous}}|$")
plt.title("Finite Square Well Grid Convergence")

plt.xscale("log", base=2)
plt.yscale("log")

plt.xticks(
    NUM_POINTS_LIST[1:],
    NUM_POINTS_LIST[1:]
)

plt.legend()
plt.grid(True, which="both")

plt.savefig(
    "figures/finite_well_convergence.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()