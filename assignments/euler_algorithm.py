import matplotlib.pyplot as plt


#An example of solving dy/dx = 2x numerically using Euler's algorithm
#Analytical solution ot the equation is x^2


def analytical_solution(x):
    return x ** 2


def f(x):
    return 2 * x
