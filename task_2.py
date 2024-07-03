import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Monte Carlo integration
def f(x):
    return x ** 0.5

# Integration bounds
a = 0
b = 2

# Monte Carlo simulation
N = 10000
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)

under_curve = y_rand < f(x_rand)
integral_mc = (b - a) * (f(b)) * np.sum(under_curve) / N

# Quad integration for comparison
result_quad, error_quad = spi.quad(f, a, b)

# Plotting the function and the Monte Carlo points
x = np.linspace(a, b, 400)
y = f(x)

plt.plot(x, y, 'r', linewidth=2)
plt.fill_between(x, y, color='green', alpha=0.3)
plt.scatter(x_rand, y_rand, c=under_curve, s=1, cmap='bwr', alpha=0.5)
plt.title(f"Monte Carlo Integration: {integral_mc}\nSciPy Quad Integration: {result_quad}")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()

# Print the results
print(f"Monte Carlo Integration result: {integral_mc}")
print(f"SciPy Quad Integration result: {result_quad}")
print(f"Difference: {abs(integral_mc - result_quad)}")