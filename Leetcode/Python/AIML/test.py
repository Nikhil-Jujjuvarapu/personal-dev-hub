import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = -x

y1 = -x          # x + y = 0
y2 = x           # x - y = 0

plt.figure(figsize=(5,5))
plt.plot(x, y1, label="x + y = 0")
plt.plot(x, y2, label="x - y = 0")

plt.scatter(0, 0, color='red', zorder=5)
plt.text(0.1, 0.1, "(0,0)", fontsize=10)

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.grid(True)
plt.axis('equal')
plt.xlim(-5,5)
plt.ylim(-5,5)

plt.legend()
plt.title("Unique Solution in Homogeneous System")
plt.show()
