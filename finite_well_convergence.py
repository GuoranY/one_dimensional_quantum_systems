import numpy as np
import matplotlib.pyplot as plt


def calculate_bound_energies(num_points):
    # Parameters
    hbar = 1
    m = 1
    L = 1
    V0 = 20

    x = np.linspace(-2, 2, num_points)
    dx = x[1] - x[0]

    V = np.where(np.abs(x) <= L / 2, 0, V0)

    main_diagonal = (
        np.full(num_points, hbar**2 / (m * dx**2))
        + V
    )

    off_diagonal = np.full(
        num_points - 1,
        -hbar**2 / (2 * m * dx**2)
    )

    H = (
        np.diag(main_diagonal)
        + np.diag(off_diagonal, 1)
        + np.diag(off_diagonal, -1)
    )

    energies, _ = np.linalg.eigh(H)

    bound_energies = energies[energies < V0]

    return bound_energies


num_points_list = [50, 100, 200, 400, 800]

ground_state_energies = []
first_excited_energies = []

for num_points in num_points_list:
    energies = calculate_bound_energies(num_points)

    ground_state_energies.append(energies[0])
    first_excited_energies.append(energies[1])

    print(
        f"N = {num_points:4d}, "
        f"E0 = {energies[0]:.8f}, "
        f"E1 = {energies[1]:.8f}"
    )

print("\nChanges between consecutive grid sizes:")

for i in range(1, len(num_points_list)):
    delta_E0 = abs(
        ground_state_energies[i]
        - ground_state_energies[i - 1]
    )

    delta_E1 = abs(
        first_excited_energies[i]
        - first_excited_energies[i - 1]
    )

    print(
        f"N = {num_points_list[i]:4d}: "
        f"|ΔE0| = {delta_E0:.8f}, "
        f"|ΔE1| = {delta_E1:.8f}"
    )

delta_E0_list = []
delta_E1_list = []

for i in range(1, len(num_points_list)):
    delta_E0_list.append(
        abs(
            ground_state_energies[i]
            - ground_state_energies[i - 1]
        )
    )

    delta_E1_list.append(
        abs(
            first_excited_energies[i]
            - first_excited_energies[i - 1]
        )
    )

plt.figure()

plt.plot(
    num_points_list[1:],
    delta_E0_list,
    "o-",
    label="Ground state"
)

plt.plot(
    num_points_list[1:],
    delta_E1_list,
    "o-",
    label="First excited state"
)

plt.xlabel("Larger grid size N")
plt.ylabel("Change in energy")
plt.title("Grid Convergence Error")
plt.yscale("log")
plt.legend()
plt.grid()

plt.savefig(
    "figures/finite_well_convergence.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()