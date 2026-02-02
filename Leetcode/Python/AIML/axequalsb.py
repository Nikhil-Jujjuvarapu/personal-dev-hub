import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([1, 2])
a2 = np.array([2, 1])

x1, x2 = 1, 1
b = x1*a1 + x2*a2
print(b)
plt.figure(figsize=(6,6))

# Column vectors
plt.arrow(0, 0, a1[0], a1[1],
          head_width=0.15, color='blue',
          length_includes_head=True)
plt.arrow(0, 0, a2[0], a2[1],
          head_width=0.15, color='red',
          length_includes_head=True)

# Linear combination (result)
plt.arrow(0, 0, b[0], b[1],
          head_width=0.15, color='green',
          length_includes_head=True)

plt.text(a1[0], a1[1], "a1", fontsize=12)
plt.text(a2[0], a2[1], "a2", fontsize=12)
plt.text(b[0], b[1], "b", fontsize=12)

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.grid(True)
plt.axis('equal')
plt.xlim(-1,5)
plt.ylim(-1,5)

plt.title("Ax = b as a Linear Combination of Columns")
plt.show()
