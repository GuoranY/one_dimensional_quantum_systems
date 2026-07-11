import numpy as np
import matplotlib.pyplot as plt

L = 1
x = np.linspace(0, L, 500)

for n in [1, 2, 3]:
    psi = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

    plt.plot(x, psi, label=f"n = {n}")

plt.xlabel("x")
plt.ylabel("psi(x)")
plt.title("Infinite Square Well Wavefunctions")
plt.grid()
plt.legend()
plt.show()


for n in [1, 2, 3]:
    psi = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
    probability = np.abs(psi) ** 2

    plt.plot(x, probability, label=f"n = {n}")

plt.xlabel("x")
plt.ylabel("|psi(x)|^2")
plt.title("Probability Densities")
plt.grid()
plt.legend()
plt.show()