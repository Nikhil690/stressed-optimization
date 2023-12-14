# Maximize Z = 3x + 2y

# Subject to the constraints:
# 2x + y ≤ 20
# 4x − 5y ≥ −10
# x + 2y ≥ 2
# x ≥ 0
# y ≥ 0

import numpy as np
import matplotlib.pyplot as plt

# Define the objective function and constraints
def objective_function(x):
    return 3 * x + 2 * (20 - 2 * x)

def constraint1(x):
    return 20 - 2 * x

def constraint2(x):
    return (4 * x + 10) / 5

def constraint3(x):
    return (2 - x) / 2

# Generate x values
x_values = np.linspace(0, 10, 400)

# Plot objective function and constraints
plt.plot(x_values, objective_function(x_values), label='Z = 3x + 2y', color='black')
plt.plot(x_values, constraint1(x_values), label='2x + y ≤ 20', linestyle='dashed')
plt.plot(x_values, constraint2(x_values), label='4x - 5y ≥ -10', linestyle='dashed')
plt.plot(x_values, constraint3(x_values), label='x + 2y ≥ 2', linestyle='dashed')

# Fill feasible region
plt.fill_between(x_values, 0, constraint1(x_values), where=(x_values >= 0) & (x_values <= 10), color='gray', alpha=0.3)
plt.fill_between(x_values, constraint2(x_values), constraint3(x_values), where=(x_values >= 0) & (x_values <= 10), color='gray', alpha=0.3)

# Add labels and legend
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Graphical Solution of LPP')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
