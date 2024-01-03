import sympy as sp

# Define the symbolic variables
x, y = sp.symbols('x y')

# Define the function
f = 100*(y-x*2)**2+(1-x)**2

# Compute the gradient
gradient = [sp.diff(f, var) for var in (x, y)]

# Compute the Hessian
hessian = [[sp.diff(gradient[i], var_j) for var_j in (x, y)] for i in range(len(gradient))]

# Print the gradient and Hessian
print("Gradient:")
print(gradient)

print("Hessian:")
for row in hessian:
    print(row)