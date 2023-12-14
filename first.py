import numpy as np
import matplotlib.pyplot as plt

def plot_constraints(constraints, x_range):
    for constraint in constraints:
        plt.plot(x_range, constraint(x_range), label=f'{constraint.__name__}(x)')

def plot_feasible_region(x_range, y_range):
    plt.fill_between(x_range, 0, y_range, color='gray', alpha=0.5, label='Feasible Region')

def solve_lpp_graphically(objective_function, constraints, x_range):
    # Plot constraints
    plot_constraints(constraints, x_range)

    # Plot the objective function
    plt.plot(x_range, objective_function(x_range), label=f'{objective_function.__name__}(x)', linestyle='dashed')

    # Find feasible region
    y_range = np.minimum.reduce([constraint(x_range) for constraint in constraints])

    # Plot feasible region
    plot_feasible_region(x_range, y_range)

    # Highlight the optimal point (minimization problem)
    optimal_x = x_range[np.argmin(objective_function(x_range))]
    optimal_y = objective_function(optimal_x)
    plt.scatter(optimal_x, optimal_y, color='red', label='Optimal Point')

    # Set plot details
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.title('Linear Programming Problem - Graphical Solution')

    # Show the plot
    plt.show()

# Example usage:
# Define the objective function and constraints
def objective_function(x):
    return 3*x + 2

def constraint1(x):
    return (4 - x) / 2

def constraint2(x):
    return (12 - 2*x) / 3

# Define the range of x values
x_range = np.linspace(0, 8, 100)

# Solve the LPP graphically
solve_lpp_graphically(objective_function, [constraint1, constraint2], x_range)
