def line_search_optimization(f, df, x0, alpha=0.01, tolerance=1e-6, max_iterations=1000):
    """
    Line Search Optimization Method

    Parameters:
    - f: Objective function
    - df: Gradient of the objective function
    - x0: Initial guess
    - alpha: Step size or learning rate
    - tolerance: Convergence tolerance
    - max_iterations: Maximum number of iterations

    Returns:
    - x_optimal: Optimal solution
    - f_optimal: Optimal function value
    """

    x = x0
    for iteration in range(max_iterations):
        gradient = df(x)

        # Check for convergence
        if abs(gradient) < tolerance:
            break

        # Update x using line search
        x = x - alpha * gradient

    return x, f(x)

# Example usage:
# Define your objective function and its gradient
def objective_function(x):
    return x**2 + 4*x + 4

def gradient(x):
    return 2*x + 4

# Initial guess
initial_guess = 0.0

# Call the line search optimization function
optimal_solution, optimal_value = line_search_optimization(objective_function, gradient, initial_guess)

# Print the results
print("Optimal Solution:", optimal_solution)
print("Optimal Value:", optimal_value)
