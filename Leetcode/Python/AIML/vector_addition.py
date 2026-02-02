import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([3, 1])
v2 = np.array([1, 2])

v_sum = v1 + v2
print(v_sum)

plt.figure(figsize=(6,6))

# v2 first
plt.arrow(0, 0, v2[0], v2[1],
          head_width=0.15, color='red',
          length_includes_head=True)

# v1 from head of v2
plt.arrow(v2[0], v2[1], v1[0], v1[1],
          head_width=0.15, color='blue',
          length_includes_head=True)

# sum
plt.arrow(0, 0, v_sum[0], v_sum[1],
          head_width=0.15, color='green',
          length_includes_head=True)

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.grid(True)
plt.axis('equal')
plt.xlim(-1,6)
plt.ylim(-1,6)

plt.title("Vector Addition is Commutative")
plt.show()

