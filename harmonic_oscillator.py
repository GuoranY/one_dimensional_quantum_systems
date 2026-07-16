import numpy as np
import matplotlib.pyplot as plt

from quantum_utils import solve_schrodinger


# Harmonic oscillator parameters

hbar = 1.0
mass = 1.0
angular_frequency = 1.0

number_of_states = 5

x_min = -6.0
x_max = 6.0
num_points = 1000

x = np.linspace(
    x_min,
    x_max,
    num_points
)


# Harmonic oscillator potential:
# V(x) = 1/2 * m * omega^2 * x^2

potential = (
    0.5
    * mass
    * angular_frequency**2
    * x**2
)


# Solve the Schrodinger equation numerically

energies, wavefunctions = solve_schrodinger(
    x=x,
    potential=potential,
    hbar=hbar,
    mass=mass,
    number_of_states=number_of_states
)


# Analytical energy eigenvalues:
# E_n = hbar * omega * (n + 1/2)

quantum_numbers = np.arange(number_of_states)

analytical_energies = (
    hbar
    * angular_frequency
    * (quantum_numbers + 0.5)
)


# Compare numerical and analytical energies

relative_errors = (
    np.abs(energies - analytical_energies)
    / analytical_energies
)

print("Harmonic oscillator energy comparison:\n")

print(
    f"{'n':>3}"
    f"{'Numerical':>15}"
    f"{'Analytical':>15}"
    f"{'Relative Error':>20}"
)

for state_index in range(number_of_states):
    print(
        f"{state_index:>3}"
        f"{energies[state_index]:>15.8f}"
        f"{analytical_energies[state_index]:>15.8f}"
        f"{relative_errors[state_index]:>20.8e}"
    )


# Plot potential, energies, and shifted wavefunctions

plt.figure(figsize=(8, 6))

plt.plot(
    x,
    potential,
    label=r"$V(x)=\frac{1}{2}m\omega^2x^2$",
    linewidth=2
)

wavefunction_scale = 0.5

for state_index in range(number_of_states):

    energy = energies[state_index]

    shifted_wavefunction = (
        energy
        + wavefunction_scale
        * wavefunctions[:, state_index]
    )

    plt.axhline(
        energy,
        linestyle="--",
        linewidth=0.8
    )

    plt.plot(
        x,
        shifted_wavefunction,
        label=f"n = {state_index}"
    )

plt.xlabel("x")
plt.ylabel("Energy")
plt.title("Quantum Harmonic Oscillator")
plt.ylim(
    0,
    analytical_energies[-1] + 1.5
)
plt.grid()
plt.legend()

plt.savefig(
    "figures/harmonic_oscillator.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()