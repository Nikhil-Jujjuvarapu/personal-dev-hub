import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 5, 100)

y1 = 4 - x        # x + y = 4
y2 = 5 - 2*x      # 2x + y = 5

plt.figure(figsize=(6,6))

# Original equations
plt.plot(x, y1, label="x + y = 4")
plt.plot(x, y2, label="2x + y = 5")

# After elimination: x = 1
plt.axvline(1, linestyle='--', label="x = 1 (pivot)")

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.grid(True)
plt.axis('equal')
plt.xlim(-1,5)
plt.ylim(-1,5)
plt.legend()
plt.title("Gaussian Elimination: Creating a Pivot")
plt.show()


plt.figure(figsize=(6,6))

plt.axvline(1, label="x = 1")
plt.axhline(3, label="y = 3")

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.grid(True)
plt.axis('equal')
plt.xlim(-1,5)
plt.ylim(-1,5)
plt.legend()
plt.title("REF/RREF: Axes-Aligned Equations")
plt.show()
