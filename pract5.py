import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import seaborn as sns

def f(x):
    return -10*np.cos(np.pi*x - 2.2) + (x + 1.5)*x

x0 = [2]
minimizer_kwargs = {"method": "BFGS"}
optimization_algorithm = opt.basinhopping(f, x0, minimizer_kwargs=minimizer_kwargs, niter=200)


optimized_x = optimization_algorithm.x
optimized_fun = optimization_algorithm.fun

print('Optimized x: ', optimized_x)
print('Optimized function value: ', optimized_fun)

sns.set_theme()

X = np.arange(-10, 10, 0.2)
Y = [f(x) for x in X]

plt.vlines(x=optimized_x, ymin=-10, ymax=125, colors='red')
plt.hlines(y=optimized_fun, xmin=-10, xmax=10, colors='red')
plt.plot(X, Y)
plt.plot(optimized_x, optimized_fun, 'o', color='black')
plt.show()