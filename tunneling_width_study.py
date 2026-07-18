import numpy as np
import matplotlib.pyplot as plt

from quantum_utils import (
    rectangular_barrier_transmission
)


# Physical parameters

hbar = 1.0
mass = 1.0

particle_energy = 1.0
barrier_height = 5.0


# Barrier widths to study

barrier_widths = np.linspace(
    0.1,
    2.0,
    100
)


# Calculate transmission coefficients

transmission_coefficients = []

for barrier_width in barrier_widths:

    transmission = rectangular_barrier_transmission(
        energy=particle_energy,
        barrier_height=barrier_height,
        barrier_width=barrier_width,
        hbar=hbar,
        mass=mass
    )

    transmission_coefficients.append(
        transmission
    )

transmission_coefficients = np.array(
    transmission_coefficients
)


# Plot transmission coefficient against barrier width

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    barrier_widths,
    transmission_coefficients
)

plt.xlabel(
    "Barrier Width"
)

plt.ylabel(
    "Transmission Coefficient"
)

plt.title(
    "Transmission Coefficient vs Barrier Width"
)

plt.grid(
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    "figures/tunneling_width_study.png",
    dpi=300
)

plt.show()


# Fit the approximately linear region of ln(T)

fit_mask = barrier_widths >= 0.5

fitted_slope, fitted_intercept = np.polyfit(
    barrier_widths[fit_mask],
    np.log(
        transmission_coefficients[fit_mask]
    ),
    1
)


# Calculate the theoretical slope

kappa = np.sqrt(
    2
    * mass
    * (
        barrier_height
        - particle_energy
    )
) / hbar

theoretical_slope = -2 * kappa


# Print slope comparison

print(
    f"Fitted slope: {fitted_slope:.6f}"
)

print(
    f"Theoretical slope: {theoretical_slope:.6f}"
)

relative_error = (
    abs(
        fitted_slope
        - theoretical_slope
    )
    / abs(
        theoretical_slope
    )
)

print(
    f"Relative error: {relative_error:.6e}"
)


# Calculate the fitted line

fitted_log_transmission = (
    fitted_slope * barrier_widths
    + fitted_intercept
)


# Plot logarithm of transmission coefficient

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    barrier_widths,
    np.log(
        transmission_coefficients
    ),
    label="Exact transmission"
)

plt.plot(
    barrier_widths,
    fitted_log_transmission,
    linestyle="--",
    label="Linear fit"
)

plt.xlabel(
    "Barrier Width"
)

plt.ylabel(
    "ln(Transmission Coefficient)"
)

plt.title(
    "Log Transmission Coefficient vs Barrier Width"
)

plt.grid(
    alpha=0.3
)

plt.legend()

plt.tight_layout()

plt.savefig(
    "figures/tunneling_width_log_study.png",
    dpi=300
)

plt.show()