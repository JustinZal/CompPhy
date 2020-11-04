from random import uniform, shuffle, random, randint
import matplotlib.pyplot as plt
import numpy as np

MAX_VELOCITY = 5


def get_cells(cars_number, cells_number, cars_in_traffic=0):
    traffic_cars = [0] * cars_in_traffic
    moving_cars = [randint(0, MAX_VELOCITY) for x in range(cars_number - cars_in_traffic)]
    empty_cells = [-1] * (cells_number - cars_number)
    basis_cells = moving_cars + empty_cells
    shuffle(basis_cells)

    return [traffic_cars + basis_cells]


def get_distance_to_next_car(cells, index):
    counter = 1

    while cells[(index + counter) % len(cells)] == -1:
        counter += 1

    return counter


def perform_simulation(moments_in_time, iterations, p):
    for i in range(iterations):
        #Take the last element
        previous_moment = moments_in_time[-1]
        current = [-1] * len(previous_moment)

        for i in range(len(previous_moment)):
            if previous_moment[i] == -1:
                continue

            v = previous_moment[i]
            distance_to_next_car = get_distance_to_next_car(previous_moment, i)
            v_temp = min(v + 1, distance_to_next_car - 1, MAX_VELOCITY)
            v = max(v_temp - 1, 0) if uniform(0, 1) < p else v_temp
            current[(i + v) % len(previous_moment)] = v

        moments_in_time.append(current)

    return moments_in_time


def prepare_plot(moments_in_time, iterations):
    canvas = np.zeros(shape=(iterations, len(moments_in_time)))
    for i in range(len(moments_in_time[0])):
        for j in range(iterations):
            canvas[j,i] = 1 if moments_in_time[j][i] > -1 else 0

    return canvas


#Simulating traffic with P = 0, 6 cars out of 18
moments_in_time = get_cells(18, 100, 6)
moments_task1 = perform_simulation(moments_in_time, 100, 0)

#Simulating the same traffic with p = 0.2
moments_in_time = get_cells(18, 100, 6)
moments_task2 = perform_simulation(moments_in_time, 100, 0.2)

#Doubling the number of cars in the model with equal p
moments_in_time = get_cells(36, 100, 12)
moments_task3 = perform_simulation(moments_in_time, 100, 0.2)


plt.imshow(moments_task3, cmap="Greys", interpolation="nearest")
plt.show()
