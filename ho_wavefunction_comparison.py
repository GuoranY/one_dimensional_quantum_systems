import math

import numpy as np
import matplotlib.pyplot as plt

from quantum_utils import solve_schrodinger


# Harmonic oscillator parameters

hbar = 1.0
mass = 1.0
angular_frequency = 1.0

number_of_states = 4

x_min = -6.0
x_max = 6.0
num_points = 1000

x = np.linspace(
    x_min,
    x_max,
    num_points
)


# Harmonic oscillator potential

potential = (
    0.5
    * mass
    * angular_frequency**2
    * x**2
)


# Numerical solution

energies, numerical_wavefunctions = solve_schrodinger(
    x=x,
    potential=potential,
    hbar=hbar,
    mass=mass,
    number_of_states=number_of_states
)


def hermite_polynomial(
    n: int,
    xi: np.ndarray
) -> np.ndarray:
    """
    Calculate the first few physicists' Hermite polynomials.
    """
    if n == 0:
        return np.ones_like(xi)

    if n == 1:
        return 2.0 * xi

    if n == 2:
        return 4.0 * xi**2 - 2.0

    if n == 3:
        return 8.0 * xi**3 - 12.0 * xi

    raise ValueError(
        "This function currently supports n = 0, 1, 2, or 3."
    )


def analytical_harmonic_wavefunction(
    x: np.ndarray,
    n: int,
    hbar: float,
    mass: float,
    angular_frequency: float
) -> np.ndarray:
    """
    Calculate an analytical harmonic oscillator wavefunction.
    """
    alpha = (
        mass
        * angular_frequency
        / hbar
    )

    xi = np.sqrt(alpha) * x

    normalization_constant = (
        (alpha / np.pi) ** 0.25
        / np.sqrt(
            2**n
            * math.factorial(n)
        )
    )

    return (
        normalization_constant
        * hermite_polynomial(n, xi)
        * np.exp(-xi**2 / 2.0)
    )


# Compare numerical and analytical wavefunctions

figure, axes = plt.subplots(
    number_of_states,
    1,
    figsize=(8, 10),
    sharex=True
)

for state_index in range(number_of_states):

    numerical_wavefunction = (
        numerical_wavefunctions[:, state_index]
    )

    analytical_wavefunction = (
        analytical_harmonic_wavefunction(
            x=x,
            n=state_index,
            hbar=hbar,
            mass=mass,
            angular_frequency=angular_frequency
        )
    )

    # Eigenvectors may differ by an overall sign.
    # Reverse the numerical sign when necessary.

    overlap = np.trapezoid(
        numerical_wavefunction
        * analytical_wavefunction,
        x
    )

    if overlap < 0:
        numerical_wavefunction = (
            -numerical_wavefunction
        )

    axes[state_index].plot(
        x,
        analytical_wavefunction,
        label="Analytical",
        linewidth=2
    )

    axes[state_index].plot(
        x,
        numerical_wavefunction,
        linestyle="--",
        label="Numerical"
    )

    axes[state_index].set_ylabel(
        rf"$\psi_{state_index}(x)$"
    )

    axes[state_index].set_title(
        f"State n = {state_index}"
    )

    axes[state_index].grid()
    axes[state_index].legend()

axes[-1].set_xlabel("x")

figure.suptitle(
    "Harmonic Oscillator Wavefunction Comparison"
)

figure.tight_layout()

plt.savefig(
    "figures/ho_wavefunction_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()