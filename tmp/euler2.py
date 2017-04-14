from __future__ import division
import numpy as np
import matplotlib.pyplot as plt



# Righthand side of differential equation
def f(y):
    return 2 * y + 7


# Define initial condition
y0 = 0.5

# Define time step
h = 0.01

# Range
ran = 2
# Define discretized time ; assumes dt divides nicely into T
t = np.linspace(0, ran, int(ran / h) + 1)

# An array to store the solution
y = np.zeros(len(t))
y[0] = y0
for i in range(1, len(t)):
    y[i] = round(y[i - 1] + f(y[i - 1]) * h,2)

plt.figure()

plt.plot(t,y, color='blue')

plt.xlabel('t')
plt.ylabel('y(t)')

plt.show()


