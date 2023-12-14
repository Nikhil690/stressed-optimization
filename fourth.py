from sympy import symbols, diff, cos, pi, solve

# Define the variable x
x = symbols('x')

# Define the objective function
f = -10 * cos(pi * x - 2.2) + (x + 1.5) * x

# Find the derivative of the function
f_prime = diff(f, x)

# Find critical points symbolically
critical_points_symbolic = solve(f_prime, x)

# Convert symbolic critical points to numerical values
critical_points = [point.evalf() for point in critical_points_symbolic]

# Evaluate the function at the critical points
objective_values = [f.evalf(subs={x: point}) for point in critical_points]

# Find the global optimal solution (minimum value)
global_optimal_value = min(objective_values)
global_optimal_solution = critical_points[objective_values.index(global_optimal_value)]

# Print the results
print("Critical Points:", critical_points)
print("Function Values at Critical Points:", [f_prime.evalf(subs={x: point}) for point in critical_points])
print("Global Optimal Solution (x):", global_optimal_solution)
print("Optimal Value:", global_optimal_value)
