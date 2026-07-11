import numpy as np
import matplotlib.pyplot as plt

L = 1

x = np.linspace(0, L, 500)

psi = np.sqrt(2 / L) * np.sin(np.pi * x / L)

plt.plot(x, psi)

plt.xlabel("x")
plt.ylabel("psi(x)")
plt.title("Ground State Wavefunction")

plt.grid()
plt.show()

probability = np.abs(psi)**2

plt.plot(x, probability)
plt.xlabel("x")
plt.ylabel("|psi(x)|^2")
plt.title("Probability Density")
plt.grid()
plt.show()