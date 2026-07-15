import numpy as np
import matplotlib.pyplot as plt

from quantum_utils import (
    solve_schrodinger,
    find_bound_states,
    determine_parity
)

hbar = 1.0
mass = 1.0

well_width = 1.0
barrier_energy = 20.0

x_min = -5.0
x_max = 5.0
num_points = 2000

x = np.linspace(
    x_min,
    x_max,
    num_points
)

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

if len(bound_energies) == 0:
    raise RuntimeError(
        "No bound states were found."
    )

print("Finite square well parity analysis:\n")

for state_index, energy in enumerate(bound_energies):
    wavefunction = bound_wavefunctions[
        :,
        state_index
    ]

    parity = determine_parity(
        wavefunction
    )

    print(
        f"State {state_index}: "
        f"E = {energy:.6f}, "
        f"parity = {parity}"
    )

    plt.plot(
        x,
        wavefunction,
        label=(
            f"State {state_index}, "
            f"{parity}"
        )
    )

plt.axvline(
    -well_width / 2,
    color="black",
    linestyle="--",
    linewidth=1
)

plt.axvline(
    well_width / 2,
    color="black",
    linestyle="--",
    linewidth=1
)

plt.xlabel("Position x")
plt.ylabel(r"$\psi(x)$")
plt.title(
    "Parity of Finite Square Well Bound States"
)
plt.grid()
plt.legend()

plt.savefig(
    "figures/finite_well_parity.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()