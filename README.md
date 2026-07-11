# One-Dimensional Quantum Systems

A Python project for computationally exploring fundamental models in one-dimensional quantum mechanics.

## Current Contents

### Infinite Square Well

- Wavefunctions for the first three energy eigenstates
- Probability densities for the first three energy eigenstates
- Energy levels for the first three states
- Analytical solutions using natural units with hbar = m = L = 1

### Finite Square Well

- Finite square well potential with adjustable width and barrier height
- Numerical bound-state energies
- Bound-state wavefunctions obtained using the finite-difference method
- Combined visualization of the potential, energy levels, and shifted wavefunctions

### Numerical Convergence

A grid-convergence test was performed for the finite square well by increasing the number of spatial grid points from 50 to 800.

The calculated bound-state energies approach stable values as the grid is refined:

- Ground-state energy: approximately 2.81
- First excited-state energy: approximately 10.73

Increasing the grid size from 400 to 800 changes both energies by approximately 0.2%, indicating reasonable numerical convergence.

## Features

- Computes analytical eigenfunctions and energies for the infinite square well
- Constructs the finite-difference Hamiltonian for the finite square well
- Solves numerically for bound-state energies and wavefunctions
- Normalizes numerical wavefunctions
- Plots potentials, wavefunctions, probability densities, and energy levels
- Performs a grid-convergence test for the numerical calculation

## Tools

- Python
- NumPy
- Matplotlib

## Units

Calculations use natural units where appropriate:

- hbar = 1
- m = 1
- L = 1 for the infinite square well

## Status

This project is currently under development.