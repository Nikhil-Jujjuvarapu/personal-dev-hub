import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 5, 100)
y = 4 - x

plt.figure(figsize=(5,5))

# Line from first equation
plt.plot(x, y, label="x + y = 4")

# Second equation: x = 1
plt.axvline(1, linestyle='--', label="x = 1")

# Intersection point
plt.scatter(1, 3, color='red', zorder=5)
plt.text(1.05, 3.05, "(1,3)", fontsize=10)

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.grid(True)
plt.axis('equal')
plt.xlim(-1,5)
plt.ylim(-1,5)

plt.legend()
plt.title("0 Free Variables → Point")
plt.show()



