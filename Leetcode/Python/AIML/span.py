import matplotlib.pyplot as plt
import numpy as np

# Our vector
v = np.array([3, 6])

# Create a range of scalars (c values) from -10 to 10
scalars = np.linspace(-10, 10, 100)

# Calculate the span (c * v)
# This creates a list of x coordinates and y coordinates
span_x = scalars * v[0]
span_y = scalars * v[1]

plt.figure(figsize=(6,6))

# Plot the infinite line (The Span)
plt.plot(span_x, span_y, color='lightblue', linestyle='--', label='Span of [3,2]')

# Plot the original vector as an arrow
plt.quiver(0, 0, v[0], v[1], color='red', angles='xy', scale_units='xy', scale=1, label='Vector [3,2]')

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(True)
plt.legend()
plt.title("The Span of a Single Vector is a Line")
plt.show()