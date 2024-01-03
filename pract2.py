import numpy as np 
import matplotlib.pyplot as plt
# Define the objective function coefficients
c = np.array ([3, 2])
# Define the constraint coefficients
A = np.array([ [2, 1], [1, 2]])
b = np.array ( [6, 4])
# Solve for the intersection points of the constraints
intersection = np.linalg.solve(A, b)
# Create a grid of x and y values for plotting
x = np.linspace(0, 4, 400)
y = np.linspace(0, 4, 400)
X, Y = np.meshgrid(x, y)
# Calculate Z (the objective function) for each point on the grid
Z = c[0]*x + c[1]*Y
# Plot the objective function Z
plt.figure(figsize=(8, 6))
plt.contour(X, Y, Z, levels=np.arange(0, Z.max()+1, 1), colors='b') 
plt.xlabel('x') 
plt.ylabel('y')
# Plot the constraint lines
plt.plot([0, intersection [0]], [6, intersection[1]], label='2x + y ≤ 6', color='r') 
plt.plot([0, intersection [0]], [2, intersection[1]], label='x + 2y ≤ 4', color='g')
# Highlight the intersection point (optimal solution)
plt.scatter(intersection[0], intersection[1], color='red', marker='o') 
plt.text(intersection[0], intersection[1], f'Optimal Point\n({intersection[0]}, ({intersection[1]})', fontsize=12, verticalalignment='bottom')
plt.xlim(0, 4) 
plt.ylim(0, 4) 
plt.legend () 
plt.grid(True)
plt.title( 'Graphical Solution of Linear Programming Problem')
plt.show()