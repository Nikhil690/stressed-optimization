#𝑓(𝑥) = 100(𝑥2 − 𝑥1^2)^2 + (1 − 𝑥1)^2

import numpy as np

def objective_function(x):
  """
  Objective function for the Rosenbrock function.

  Args:
    x: A numpy array representing the input vector (x1, x2).

  Returns:
    The value of the function at x.
  """
  x1, x2 = x
  return 100 * (x2 - x1**2)**2 + (1 - x1)**2

def gradient_function(x):
  """
  Calculates the gradient of the objective function.

  Args:
    x: A numpy array representing the input vector (x1, x2).

  Returns:
    The gradient of the function at x as a numpy array.
  """
  x1, x2 = x
  return np.array([
      400 * x1 * (x2 - x1**2) - 2 * (1 - x1),
      200 * (x2 - x1**2)
  ])

def hessian_function(x):
  """
  Calculates the Hessian of the objective function.

  Args:
    x: A numpy array representing the input vector (x1, x2).

  Returns:
    The Hessian of the function at x as a 2x2 numpy array.
  """
  x1, x2 = x
  return np.array([
      [1200 * (x2 - x1**2) - 4, -400 * (x2 - x1)],
      [-400 * (x2 - x1), 200]
  ])

# Example usage
x = np.array([1.0, 2.0])
objective_value = objective_function(x)
gradient = gradient_function(x)
hessian = hessian_function(x)

print(f"Objective function value at x = {x}: {objective_value}")
print(f"Gradient at x = {x}: {gradient}")
print(f"Hessian at x = {x}:")
print(hessian)
