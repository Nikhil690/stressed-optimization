#𝑓(𝑥) = −10𝐶𝑜𝑠(𝜋𝑥 − 2.2) + (𝑥 + 1.5)𝑥

import numpy as np
import matplotlib.pyplot as plt

# Define the objective function
def objective_function(x):
    return -10 * np.cos(np.pi * x - 2.2) + (x + 1.5) * x

# Define the range of x values
x_range = np.linspace(-5, 5, 100)

# Plot the objective function
plt.plot(x_range, objective_function(x_range), label='f(x)')

# Find the global optimal solution (minimum) using numpy
optimal_x = np.argmin(objective_function(x_range))
optimal_solution = x_range[optimal_x]
optimal_value = objective_function(optimal_solution)

# Highlight the optimal point
plt.scatter(optimal_solution, optimal_value, color='red', label='Global Optimal Solution')

# Set plot details
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.title('Global Optimal Solution - Graphical Method')

# Show the plot
plt.show()

# Print the results
print("Global Optimal Solution (x):", optimal_solution)
print("Optimal Value:", optimal_value)
