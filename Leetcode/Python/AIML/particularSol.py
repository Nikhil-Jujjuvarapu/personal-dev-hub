import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

# Homogeneous system
y_h = -x           # x + y = 0

# Non-homogeneous system
y_p = 4 - x        # x + y = 4

plt.figure(figsize=(5,5))
plt.plot(x, y_h, label="Ax = 0  →  x + y = 0")
plt.plot(x, y_p, label="Ax = b  →  x + y = 4")

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.grid(True)
plt.axis('equal')
plt.xlim(-5,5)
plt.ylim(-5,5)

plt.legend()
plt.title("Homogeneous vs Non-Homogeneous Solutions")
plt.show()


plt.figure(figsize=(5,5))
plt.plot(x, y_p, label="x + y = 4")
plt.scatter(4, 0, color='red', zorder=5)
plt.text(4.1, 0.1, "particular solution", fontsize=10)

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.grid(True)
plt.axis('equal')
plt.xlim(-1,6)
plt.ylim(-1,6)

plt.legend()
plt.title("Particular Solution")
plt.show()
