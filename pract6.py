from scipy.optimize import minimize

# Define the objective function to minimize
def objective_function(x):
    return x[0]*2 + x[1]*2  # Example: minimize x^2 + y^2

# Define the constraint function
def constraint_function(x):
    return x[0] + x[1] - 1  # Example: x + y = 1

# Set initial guess
initial_guess = [0, 0]

# Define the constraint as a dictionary
constraint = {'type': 'eq', 'fun': constraint_function}

# Use the minimize function with method='SLSQP' (Sequential Least SQuares Programming)
result = minimize(objective_function, initial_guess, constraints=constraint, method='SLSQP')

# Print the result
print("Optimal solution:", result.x)
print("Optimal value:", result.fun)