import numpy as np
import matplotlib.pyplot as plt

# Finite square well parameters
L = 1
V0 = 20

x = np.linspace(-2, 2, 1000)

# Potential:
# V(x) = 0 inside the well
# V(x) = V0 outside the well
V = np.where(np.abs(x) <= L / 2, 0, V0)

plt.plot(x, V)

plt.xlabel("x")
plt.ylabel("V(x)")
plt.title("Finite Square Well Potential")
plt.ylim(-2, V0 + 5)
plt.grid()

plt.show()