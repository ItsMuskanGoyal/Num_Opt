# WAP to find Global Optimal Solution of a function
# f(x) = −10Cos(πx − 2.2) + (x + 1.5)x algebraically

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import seaborn as sns

def f(x):
    return -10*np.cos(np.pi*x - 2.2) + (x + 1.5)*x

x0 = [2]
minimizer_kwargs = {"method": "BFGS"}
optimization_algorithm = opt.basinhopping(f, x0, minimizer_kwargs=minimizer_kwargs, niter=200)

print('1-D function')
print(optimization_algorithm.message[0])

optimized_x = optimization_algorithm.x
optimized_fun = optimization_algorithm.fun

print('Optimized x: ', optimized_x)
print('Optimized function value: ', optimized_fun)