# One-Dimensional Quantum Systems

A Python project for computationally exploring fundamental models in one-dimensional quantum mechanics using analytical
solutions and numerical finite-difference methods.

## Current Contents

### Infinite Square Well

The infinite square well is studied analytically using exact energy eigenfunctions and energy eigenvalues.

Current calculations include:

- Analytical wavefunctions for the first three energy eigenstates
- Probability densities for the first three energy eigenstates
- Energy levels for the first three states
- Calculations use natural units with $\hbar = m = L = 1$

#### Wavefunctions

![Infinite square well wavefunctions](figures/infinite_well_wavefunctions.png)

#### Probability Densities

![Infinite square well probability densities](figures/infinite_well_probability_density.png)

#### Energy Levels

![Infinite square well energy levels](figures/infinite_well_energy_levels.png)

### Finite Square Well

The finite square well is solved numerically using the finite-difference method.

The continuous Hamiltonian operator

$$
\hat{H}
=
-\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)
$$

is approximated by a symmetric tridiagonal matrix on a uniformly spaced spatial grid. Numerical diagonalization is then
used to obtain the energy eigenvalues and eigenfunctions.

Current calculations include:

- A finite square well potential with adjustable width and barrier height
- Construction of the finite-difference Hamiltonian matrix
- Numerical calculation of energy eigenvalues and eigenfunctions
- Identification of bound states with energies below the external barrier
- Bound-state wavefunctions obtained using the finite-difference method
- Numerical normalization of wavefunctions
- Visualization of the potential, energy levels, and shifted wavefunctions

#### Potential

![Finite square well potential](figures/finite_well_potential.png)

#### Bound-State Wavefunctions

![Finite square well wavefunctions](figures/finite_well_wavefunctions.png)

#### Bound States and Energy Levels

![Finite square well bound states](figures/finite_well_bound_states.png)

### Numerical Convergence

A grid-convergence test was performed for the finite square well by increasing the number of spatial grid points.

The calculated bound-state energies approach stable values as the grid is refined.

For the selected well parameters:

- Ground-state energy: approximately $2.81$
- First excited-state energy: approximately $10.73$

Increasing the grid points from 400 to 800 changes both energies by approximately $0.2%$, indicating reasonable numerical
convergence.

![Finite well convergence test](figures/finite_well_convergence.png)

### Effect of Well Depth

The barrier height $V_0$ was varied while the well width was kept fixed.

The number of numerical bound states increases as the well becomes deeper:

- $V_0 = 5$: 1 bound state
- $V_0 = 10$: 2 bound states
- $V_0 = 20$: 2 bound states
- $V_0 = 40$: 3 bound states
- $V_0 = 80$: 4 bound states

This demonstrates that deeper finite wells can support more bound states.

![Bound states versus barrier height](figures/bound_states_vs_depth.png)

## Numerical Methods

The finite square well calculations use a central finite-difference approximation for the second derivative:

$$
\frac{d^2\psi}{dx^2}
\approx
\frac{\psi_{i+1}-2\psi_i+\psi_{i-1}}
{\Delta x^2}
$$

This produces a Hamiltonian matrix with:

- Kinetic energy and potential energy terms on the main diagonal
- Finite-difference coupling terms on the first upper and lower diagonal

Because the Hamiltonian matrix is real and symmetric, its eigenvalues and eigenvectors are calculated using
'numpy.linalg.eigh'.

The numerical eigenfunctions are normalized according to

$$
\int |\psi(x)|^2\,dx = 1
$$

## Shared Numerical Utilities

Reusable numerical functions are stored in 'quantum_utils.py'.

These utilities include:

- Validation of one-dimensional spatial grids
- Construction of finite-difference Hamiltonian matrices
- Numerical solution of the time-independent Schrödinger equation
- Numerical normalization of eigenfunctions
- Identification of bound states below a specified energy threshold

Using shared utility functions reduces duplicated code and keeps the individual simulation scripts focused on the
physical systems being studied.

## Features

- Computes analytical eigenfunctions and energies for the infinite square well
- Calculates probability densities for analytical wavefunctions
- Constructs finite-difference Hamiltonian matrices for the finite square well
- Solves the time-independent Schrödinger equation numerically
- Calculates bound-state energies and wavefunctions
- Normalizes numerical wavefunctions using numerical integration
- Identifies bound states using an energy threshold
- Plots potentials, wavefunctions, probability densities, and energy levels
- Performs a grid-convergence test for the numerical calculation
- Investigates how well depth affects the number of bound states
- Uses reusable numerical functions through a shared utility module

## Tools

- Python
- NumPy
- Matplotlib

## Units

For simplification, calculations use natural units where appropriate:

- $\hbar = 1$
- $m = 1$
- $L = 1$ for the infinite square well

## Project Structure

```text
one_dimensional_quantum_systems/
├── figures/
│   ├── bound_states_vs_depth.png
│   ├── finite_well_bound_states.png
│   ├── finite_well_convergence.png
│   ├── finite_well_potential.png
│   ├── finite_well_wavefunctions.png
│   ├── infinite_well_energy_levels.png
│   ├── infinite_well_probability_density.png
│   └── infinite_well_wavefunctions.png
├── finite_square_well.py
├── finite_well_convergence.py
├── finite_well_depth_study.py
├── infinite_square_well.py
├── quantum_utils.py
├── .gitignore
└── README.md
```

## Status

This project is currently under development.