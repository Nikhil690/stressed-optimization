import numpy as np
from scipy.optimize import minimize_scalar

# Define the objective function
def objective_function(x):
    return -10 * np.cos(np.pi * x - 2.2) + (x + 1.5) * x

# Line search function
def line_search_method(obj_func, initial_guess):
    result = minimize_scalar(obj_func, method='bounded', bounds=(-5, 5))
    optimal_solution = result.x
    optimal_value = result.fun
    return optimal_solution, optimal_value

# Initial guess
initial_guess = 0

# Apply Line Search method
optimal_solution, optimal_value = line_search_method(objective_function, initial_guess)

# Print the results
print("Global Optimal Solution (x):", optimal_solution)
print("Optimal Value:", optimal_value)
