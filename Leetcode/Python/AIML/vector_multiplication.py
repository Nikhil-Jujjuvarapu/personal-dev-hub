import numpy as np
import matplotlib.pyplot as plt

v = np.array([3, 1])

plt.figure(figsize=(6,6))

# original vector
plt.arrow(0, 0, v[0], v[1],
          head_width=0.15, color='blue',
          length_includes_head=True)

# scaled by 2
plt.arrow(0, 0, 2*v[0], 2*v[1],
          head_width=0.15, color='green',
          length_includes_head=True)

# scaled by -1 (flip)
plt.arrow(0, 0, -v[0], -v[1],
          head_width=0.15, color='red',
          length_includes_head=True)

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.grid(True)
plt.axis('equal')
plt.xlim(-10,10)
plt.ylim(-10,10)

plt.title("Scalar Multiplication: Stretch & Flip")
plt.show()
