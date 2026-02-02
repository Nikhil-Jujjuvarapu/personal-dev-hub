import matplotlib.pyplot as plt
import numpy as np

# First arrow: from (0,0) to (3,2)
start1 = np.array([0, 0])
end1   = np.array([3, 2])
vec1   = end1 - start1

# Second arrow: from (5,1) to (8,3)
start2 = np.array([5, 1])
end2   = np.array([8, 3])
vec2   = end2 - start2

plt.figure(figsize=(6,6))

# Draw arrows
plt.arrow(start1[0], start1[1], vec1[0], vec1[1],
          head_width=0.2, length_includes_head=True, color='blue')
plt.arrow(start2[0], start2[1], vec2[0], vec2[1],
          head_width=0.2, length_includes_head=True, color='red')


#magnitude
magnitude = np.linalg.norm(vec1)
print(magnitude)
magnitude2 = np.linalg.norm(vec2)
print(magnitude2)


#direction
angle_rad = np.arctan2(vec1[1], vec1[0])
angle_deg = np.degrees(angle_rad)

print(angle_deg)

#unit vector - when you only need direction
unit_vector = vec1 / np.linalg.norm(vec1)
print(unit_vector)
plt.arrow(0,0,unit_vector[0],unit_vector[1], head_width=0.5, length_includes_head=True, color = 'purple')


# Draw points
plt.scatter(*start1, color='blue')
plt.scatter(*start2, color='red')

# Axes settings
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True)
plt.axis('equal')
plt.xlim(-1,10)
plt.ylim(-1,6)

plt.title("Two arrows representing the same vector")
plt.show()

