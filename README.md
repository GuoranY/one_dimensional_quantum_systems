# One-Dimensional Quantum Systems

A Python project for computationally exploring fundamental models in one-dimensional quantum mechanics.

## Current Contents

### Infinite Square Well

- Analytical wavefunctions for the first three energy eigenstates
- Probability densities for the first three energy eigenstates
- Energy levels for the first three states
- Calculations use natural units with hbar = m = L = 1

#### Wavefunctions

![Infinite square well wavefunctions](figures/infinite_well_wavefunctions.png)

#### Probability Densities

![Infinite square well probability densities](figures/infinite_well_probability_density.png)

#### Energy Levels

![Infinite square well energy levels](figures/infinite_well_energy_levels.png)

### Finite Square Well

- Finite square well potential with adjustable width and barrier height
- Numerical bound-state energies
- Bound-state wavefunctions obtained using the finite-difference method
- Combined visualization of the potential, energy levels, and shifted wavefunctions

#### Potential

![Finite square well potential](figures/finite_well_potential.png)

#### Bound-State Wavefunctions

![Finite square well wavefunctions](figures/finite_well_wavefunctions.png)

#### Bound States and Energy Levels

![Finite square well bound states](figures/finite_well_bound_states.png)

### Numerical Convergence

A grid-convergence test was performed for the finite square well by increasing the number of spatial grid points from 50 to 800.

The calculated bound-state energies approach stable values as the grid is refined:

- Ground-state energy: approximately 2.81
- First excited-state energy: approximately 10.73

Increasing the grid size from 400 to 800 changes both energies by approximately 0.2%, indicating reasonable numerical convergence.

![Finite well convergence test](figures/finite_well_convergence.png)

### Effect of Well Depth

The barrier height \(V_0\) was varied while the well width was kept fixed.

The number of numerical bound states increases as the well becomes deeper:

- \(V_0 = 5\): 1 bound state
- \(V_0 = 10\): 2 bound states
- \(V_0 = 20\): 2 bound states
- \(V_0 = 40\): 3 bound states
- \(V_0 = 80\): 4 bound states

This demonstrates that deeper finite wells can support more bound states.

![Bound states versus barrier height](figures/bound_states_vs_depth.png)

## Features

- Computes analytical eigenfunctions and energies for the infinite square well
- Calculates probability densities for analytical wavefunctions
- Constructs a finite-difference Hamiltonian for the finite square well
- Solves numerically for bound-state energies and wavefunctions
- Normalizes numerical wavefunctions using numerical integration
- Plots potentials, wavefunctions, probability densities, and energy levels
- Performs a grid-convergence test for the numerical calculation

## Tools

- Python
- NumPy
- Matplotlib

## Units

Calculations use natural units where appropriate:

- \(hbar = 1\)
- \(m = 1\)
- \(L = 1\) for the infinite square well

## Project Structure

```text
one_dimensional_quantum_systems/
├── figures/
│   ├── finite_well_bound_states.png
│   ├── finite_well_convergence.png
│   ├── finite_well_potential.png
│   ├── finite_well_wavefunctions.png
│   ├── infinite_well_energy_levels.png
│   ├── infinite_well_probability_density.png
│   └── infinite_well_wavefunctions.png
├── finite_square_well.py
├── finite_well_convergence.py
├── infinite_square_well.py
├── .gitignore
└── README.md
```

## Status

This project is currently under development.