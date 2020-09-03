import matplotlib.pyplot as plt
import numpy as np

#An example of solving dy/dx = 2x numerically using Euler's algorithm
#Initial condition is y(0) = 0
#Analytical solution ot the equation is x^2


def analytical_solution(x):
    return x ** 2


def f(x):
    return 2 * x


delta_x = 0.001
y0 = yn = 0
function_range = range(1, 100000)

x_range = [delta_x * x for x in function_range]
numerical_y = []

for x in x_range:
    ynp1 = yn + f(x) * delta_x
    numerical_y.append(ynp1)
    yn = ynp1


analytical_y = [analytical_solution(x) for x in x_range]
x_range = np.array(x_range)

fig, axs = plt.subplots(2)

axs[0].plot(x_range, np.array(analytical_y), 'o', color='blue')
axs[0].set_title('Analytical solution')

axs[1].plot(x_range, np.array(numerical_y), 'o', color='red')
axs[1].set_title('Numerical solution')

fig.tight_layout()

plt.show()
