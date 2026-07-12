import numpy as np
import matplotlib.pyplot as plt

hbar = 1
m = 1
L = 1

num_points = 800
x = np.linspace(-2, 2, num_points)
dx = x[1] - x[0]

V0_values = [5, 10, 20, 40, 80]

bound_state_counts = []

for V0 in V0_values:
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

    energies = np.linalg.eigvalsh(H)
    bound_energies = energies[energies < V0]

    bound_state_counts.append(len(bound_energies))

    print(
        f"V0 = {V0:4}, "
        f"number of bound states = {len(bound_energies)}"
    )

plt.figure()

plt.plot(
    V0_values,
    bound_state_counts,
    "o-"
)

plt.xlabel("Barrier height V0")
plt.ylabel("Number of bound states")
plt.title("Number of Bound States vs Barrier Height")
plt.yticks(range(min(bound_state_counts), max(bound_state_counts) + 1))
plt.grid()

plt.savefig(
    "figures/bound_states_vs_depth.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()