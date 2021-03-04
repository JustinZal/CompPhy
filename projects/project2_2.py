import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return 2 * (x ** 2) + 3 * x * y + (y ** 2)


def H(x, y):
    return int(x ** 2 + y ** 2 <= 0.5 ** 2)


def midpoint_integrate(h):
    n_x = n_y = 1/h # 0.5 - (-0.5)
    s = 0

    for i in range(int(n_x) + 1):
        for j in range(int(n_y) + 1):
            x_i = -0.5 + (i - 0.5) * h
            y_j = -0.5 + (j - 0.5) * h

            s += f(x_i, y_j) * H(x_i, y_j) * h * h

    return s


def generate_montecarlo_points(h):
    number_of_points = int((1/h) ** 2)
    points = []

    for _ in range(number_of_points):
        while True:
            x = np.random.uniform(-0.5 , 0.5)
            y = np.random.uniform(-0.5, 0.5)

            if bool(H(x, y)):
                points.append((x, y))
                break

    return points


def montecarlo_integrate(h, repetitions=10):
    A = np.pi * (0.5 ** 2)
    results = []

    for _ in range(repetitions):
        points = generate_montecarlo_points(h)
        r = (A/len(points)) * sum([f(p[0], p[1]) for p in points])
        results.append(r)

    return results



steps = [0.1, 0.05, 0.025, 0.0125]

midpoint_integrals = [midpoint_integrate(step) for step in steps]
print(midpoint_integrals, 'Midpoint integration results')

montecarlo_integrals = [montecarlo_integrate(step, 1)[0] for step in steps]
print(montecarlo_integrals, 'Monte Carlo integration results')

#Calculating errors here

err_montecarlo = [np.var(montecarlo_integrate(step, 100)) for step in steps]
err_midpoint = [1/((1/step) ** 2)  for step in steps]

print(err_midpoint, 'Midpoint errors')
print(err_montecarlo, 'Monte Carlo errors')