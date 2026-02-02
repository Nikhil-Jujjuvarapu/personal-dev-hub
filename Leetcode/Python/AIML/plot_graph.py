import matplotlib.pyplot as plt
import numpy as np

def plot_custom_data(x_points, y_points, weight, bias):
    """
    Plots a set of points and a line y = weight * x + bias.
    """
    # 1. Setup the plot area
    plt.figure(figsize=(10, 6))
    
    # 2. Plot the points (scatter plot)
    plt.scatter(x_points, y_points, color='red', label='Data Points', s=100, zorder=5)
    
    # 3. Add labels to each point for clarity
    for (xi, yi) in zip(x_points, y_points):
        plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", 
                     xytext=(0,10), ha='center', fontsize=9)

    # 4. Generate the line based on the weight and bias
    # We find the min and max x to make sure the line covers the points
    x_min, x_max = min(x_points) - 2, max(x_points) + 2
    x_range = np.linspace(x_min, x_max, 100)
    y_range = weight * x_range + bias
    
    # 5. Plot the line
    plt.plot(x_range, y_range, color='blue', linestyle='--', 
             label=f'Line: y = {weight}x + ({bias})')
    
    # 6. Formatting the graph
    plt.axhline(0, color='black', linewidth=1) # X-axis
    plt.axvline(0, color='black', linewidth=1) # Y-axis
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.xlabel('Input (x)')
    plt.ylabel('Output (y)')
    plt.title('Point Plotter & Linear Boundary')
    plt.legend()
    
    # Show the result
    plt.show()

# ==========================================
# CHANGE THESE VALUES TO EXPERIMENT:
# ==========================================
# Your coordinates
x_values = [1,3]
y_values = [3,4]

# Your Perceptron-style parameters
w = 2   # Try changing this to 1.5 or -1
b = 0   # Try changing this to 5 or -2

plot_custom_data(x_values, y_values, w, b)