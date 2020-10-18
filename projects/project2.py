import numpy as np
import matplotlib.pyplot as plt

sin = np.sin
cos = np.cos
pi = np.pi

#General variables
g = 9.8
delta_x = 0.001


def get_acceleration(vx, vy, k, n):
    v_norm = (vx **2 + vy ** 2) ** 0.5
    coef = -1 * (v_norm ** (n - 1)) * k

    return coef * vx, coef * vy - g


def solve_euler(n, k, v0, theta):
    vy0 = sin(theta) * v0
    vx0 = cos(theta) * v0

    delta_t = 0.001
    #Generate time interval
    time = [delta_t * x for x in range(0, 100000)]

    xn = 0
    yn = 0

    vxn = vx0
    vyn = vy0
    axn , ayn = get_acceleration(vxn, vyn, k, n)

    acceleration = [(axn, ayn)]
    velocity = [(vxn, vyn)]
    distance = [(xn, yn)]

    for t in time:
        vy = vyn + ayn * delta_t
        y = yn + vy * delta_t

        vx = vxn + axn * delta_t
        x = xn + vx * delta_t

        ax, ay = get_acceleration(vx, vy, k, n)

        acceleration.append((ax, ay))
        velocity.append((vx, vy))
        distance.append((x, y))

        vxn = vx
        vyn = vy
        yn = y
        xn = x
        axn = ax
        ayn = ay



    distance = list(filter(lambda x : x[1] >= 0, distance))
    d_l = len(distance)
    velocity = velocity[0:d_l]
    acceleration = acceleration[0:d_l]

    return distance, velocity, acceleration


#Part B
n = 1
k = 0.8
v0 = 22
theta = (pi / 180) * 34


#Solution for 1st equation
r, v, a = solve_euler(n, k, v0, theta)

#Part C.1
n = 1.5
k = 0.18


#Solution for second equation
r, v, a = solve_euler(n, k, v0, theta)

plt.plot(np.array([x[0] for x in r]), np.array([x[1] for x in r]))
# plt.show()

#Part C.2
n = 2
k = 0.036

#Solution for third equation
r, v, a = solve_euler(n, k, v0, theta)

plt.plot(np.array([x[0] for x in r]), np.array([x[1] for x in r]))

# Uncomment to see 3 graphs
plt.show()


#Part D

#g, and angle theta will remain fixed. k, adjusted for fixed initial force 17.6
#Varying parameters: V0, n
#Adjusting for same initial force F0 = 100N

r, v, a = solve_euler(1.2, 100 / (55 ** 1.2), 55, theta)
r1, v1, a1 = solve_euler(2.2, 100 / (120 ** 2.2), 120, theta)
r2, v2, a2 = solve_euler(2.4, 100 / (150 ** 2.4), 150, theta)

plt.plot(np.array([x[0] for x in r]), np.array([x[1] for x in r]), color='red')
plt.plot(np.array([x[0] for x in r1]), np.array([x[1] for x in r1]), color='green')
plt.plot(np.array([x[0] for x in r2]), np.array([x[1] for x in r2]), color = 'blue')

plt.show()
