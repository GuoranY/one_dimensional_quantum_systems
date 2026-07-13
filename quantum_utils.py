import numpy as np


def validate_grid(x: np.ndarray) -> float:
    """
    Check whether x is a valid uniformly spaced one-dimensional grid and
    return the grid spacing dx.
    """
    x = np.asarray(x, dtype=float)

    if x.ndim != 1:
        raise ValueError("x must be a one-dimensional array.")

    if len(x) < 3:
        raise ValueError("x must contain at least three grid points.")

    spacings = np.diff(x)

    if not np.allclose(spacings, spacings[0]):
        raise ValueError("x must be uniformly spaced.")

    if spacings[0] <= 0:
        raise ValueError("x must be strictly increasing.")

    return float(spacings[0])


def build_hamiltonian(
    x: np.ndarray,
    potential: np.ndarray,
    hbar: float = 1.0,
    mass: float = 1.0
) -> np.ndarray:
    """
    Construct the finite-difference Hamiltonian matrix for a
    one-dimensional quantum system.
    """
    x = np.asarray(x, dtype=float)
    potential = np.asarray(potential, dtype=float)

    dx = validate_grid(x)
    number_of_points = len(x)

    if potential.shape != x.shape:
        raise ValueError(
            "potential must have the same shape as x."
        )

    if mass <= 0:
        raise ValueError("mass must be positive.")

    kinetic_diagonal = (
        hbar**2 / (mass * dx**2)
    )

    kinetic_off_diagonal = (
        -hbar**2 / (2 * mass * dx**2)
    )

    main_diagonal = (
        np.full(number_of_points, kinetic_diagonal)
        + potential
    )

    off_diagonal = np.full(
        number_of_points - 1,
        kinetic_off_diagonal
    )

    hamiltonian = (
        np.diag(main_diagonal)
        + np.diag(off_diagonal, k=1)
        + np.diag(off_diagonal, k=-1)
    )

    return hamiltonian


def normalize_wavefunction(x: np.ndarray, psi: np.ndarray) -> np.ndarray:
    """
    Normalize a wavefunction numerically.
    """
    x = np.asarray(x, dtype=float)
    psi = np.asarray(psi)

    if psi.shape != x.shape:
        raise ValueError("psi must have the same shape as x.")

    probability_integral = np.trapezoid(
        np.abs(psi) ** 2,
        x
    )

    if probability_integral <= 0:
        raise ValueError(
            "The wavefunction cannot be normalized."
        )

    normalization_constant = np.sqrt(
        probability_integral
    )

    return psi / normalization_constant


def solve_schrodinger(
    x: np.ndarray,
    potential: np.ndarray,
    hbar: float = 1.0,
    mass: float = 1.0,
    number_of_states: int | None = None
) -> tuple[np.ndarray, np.ndarray]:
    """
    Solve the time-independent one-dimensional Schrodinger equation
    using the finite-difference method.
    """
    hamiltonian = build_hamiltonian(
        x=x,
        potential=potential,
        hbar=hbar,
        mass=mass
    )

    energies, wavefunctions = np.linalg.eigh(
        hamiltonian
    )

    if number_of_states is not None:
        if not isinstance(number_of_states, int):
            raise TypeError(
                "number_of_states must be an integer or None."
            )

        if number_of_states <= 0:
            raise ValueError(
                "number_of_states must be positive."
            )

        energies = energies[:number_of_states]
        wavefunctions = wavefunctions[:, :number_of_states]

    for state_index in range(wavefunctions.shape[1]):
        wavefunctions[:, state_index] = (
            normalize_wavefunction(
                x,
                wavefunctions[:, state_index]
            )
        )

    return energies, wavefunctions


def find_bound_states(
    energies: np.ndarray,
    wavefunctions: np.ndarray,
    barrier_energy: float
) -> tuple[np.ndarray, np.ndarray]:
    """
    Select bound states whose energies lie below the barrier energy.
    This is suitable for a finite square well where the potential
    outside the well is equal to barrier_energy.
    """
    energies = np.asarray(energies)
    wavefunctions = np.asarray(wavefunctions)

    if wavefunctions.ndim != 2:
        raise ValueError(
            "wavefunctions must be a two-dimensional array."
        )

    if wavefunctions.shape[1] != len(energies):
        raise ValueError(
            "The number of wavefunctions must match "
            "the number of energies."
        )

    bound_mask = energies < barrier_energy

    bound_energies = energies[bound_mask]
    bound_wavefunctions = wavefunctions[:, bound_mask]

    return bound_energies, bound_wavefunctions


def probability_density(psi: np.ndarray) -> np.ndarray:
    """
    Calculate the probability density |psi|^2.
    """
    psi = np.asarray(psi)

    return np.abs(psi) ** 2