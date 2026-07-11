import numpy as np
import matplotlib.pyplot as plt

# Infinite square well parameters
L = 1
x = np.linspace(0, L, 500)
n_values = [1, 2, 3]

# Wavefunctions
for n in n_values:
    psi = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
    plt.plot(x, psi, label=f"n = {n}")

plt.xlabel("x")
plt.ylabel(r"$\psi_n(x)$")
plt.title("Infinite Square Well Wavefunctions")
plt.grid()
plt.legend()

plt.savefig(
    "figures/infinite_well_wavefunctions.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Probability densities
for n in n_values:
    psi = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
    probability = np.abs(psi) ** 2
    plt.plot(x, probability, label=f"n = {n}")

plt.xlabel("x")
plt.ylabel(r"$|\psi_n(x)|^2$")
plt.title("Probability Densities")
plt.grid()
plt.legend()

plt.savefig(
    "figures/infinite_well_probability_density.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Energy level diagram in natural units
hbar = 1
m = 1

for n in n_values:
    energy = n**2 * np.pi**2 * hbar**2 / (2 * m * L**2)

    plt.hlines(
        energy,
        xmin=0,
        xmax=1,
        label=f"n = {n}"
    )

plt.xlim(0, 1.3)
plt.xlabel("State")
plt.ylabel(r"$E_n$ (natural units)")
plt.title("Infinite Square Well Energy Levels")
plt.grid(axis="y")
plt.legend()

plt.savefig(
    "figures/infinite_well_energy_levels.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()