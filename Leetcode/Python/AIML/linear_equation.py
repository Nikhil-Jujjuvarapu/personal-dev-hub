import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 5, 100)
y = 4 - x
x1 = np.linspace(-1, 5, 100)
y1= 5-2*x1

plt.figure(figsize=(6,6))
plt.plot(x, y, label="x + y = 4")
plt.plot(x1, y1, label="2x + y = 5")

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.grid(True)
plt.axis('equal')
plt.xlim(-1,5)
plt.ylim(-1,5)
plt.legend()
plt.title("Linear Equation as a Line")
plt.show()
