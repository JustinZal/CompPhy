import numpy as np
import matplotlib.pyplot as plt


#m^3/kg * 1/(s^2)
G = 6.67 * 10 ** (-11)
#Kg
M = 5.99 * 10 ** 24
#m
R = 6370 * 10**3
#Kg/m
k = 3 * (10 ** (-4))
#m
h = 10000
#Kg
m = 1


def gravitational_acceleration(y):
    return (G * M) / ((R + y) ** 2)


def get_damping_force(v):
    return k * (v ** 2)


delta_t = 0.001
#Generate time interval
time = [delta_t * x for x in range(0, 100000)]

xn = h
vn = 0
an = (get_damping_force(vn) / m) - gravitational_acceleration(xn)

acceleration = [an]
velocity = [vn]
distance = [xn]

#Start applying Euler method
for t in time:
    #Get values
    v = vn + an * delta_t
    x = xn + v * delta_t
    a = (get_damping_force(vn) / m) - gravitational_acceleration(xn)

    #Append values to arrays
    acceleration.append(a)
    velocity.append(v)
    distance.append(x)

    #Assign values for next iteration
    vn = v
    xn = x
    an = a

#Filter non-positive Distances to ground
distance = list(filter(lambda x: x >= 0, distance))
distance_length = len(distance)

#Take corresponding velocity and acceleration
velocity = velocity[0:distance_length]
acceleration = acceleration[0:distance_length]
time = np.array(time[0:distance_length])

#Plot values for Euler method
fig, axs = plt.subplots(3)

fig.suptitle('Euler method')

axs[0].plot(time, np.array(acceleration), color='green')
axs[0].set(title='Acceleration',
       xlabel='time (s)', ylabel=r'$\frac{m}{s^2}$')

axs[1].plot(time, np.array(velocity), color='red')
axs[1].set(title='Velocity',
       xlabel='time (s)', ylabel=r'$\frac{m}{s}$')

axs[2].plot(time, np.array(distance), color='blue')
axs[2].set(title='Distance',
       xlabel='time (s)', ylabel='m')

fig.tight_layout()


#Euler - Richardson Scheme

#Generate time for Euler - Richardson Scheme
time = [delta_t * x for x in range(0, 100000)]
xn = h
vn = 0
an = (get_damping_force(vn) / m) - gravitational_acceleration(xn)

acceleration = [an]
velocity = [vn]
distance = [xn]

#Euler-Richardson iterations
for t in time:
    #Get mid variables
    v_mid = vn + 0.5 * an * delta_t
    x_mid = xn + 0.5 * vn * delta_t
    a_mid = (get_damping_force(v_mid) / m) - gravitational_acceleration(x_mid)

    #Get variables
    v = vn + a_mid * delta_t
    x = xn + v_mid * delta_t
    a = (get_damping_force(v) / m) - gravitational_acceleration(x)

    #Collect them to array
    acceleration.append(a)
    velocity.append(v)
    distance.append(x)

    #set variables for next iteration
    vn = v
    xn = x
    an = a

#Filter non-positive Distances to ground
distance = list(filter(lambda x: x >= 0, distance))
distance_length = len(distance)

#Take corresponding velocity and acceleration
velocity = velocity[0:distance_length]
acceleration = acceleration[0:distance_length]
time = np.array(time[0:distance_length])

#Plot Euler-Richardson iterations
fig, axs = plt.subplots(3)

fig.suptitle('Euler - Richardson scheme')

axs[0].plot(time, np.array(acceleration), color='green')
axs[0].set(title='Acceleration2',
       xlabel='time (s)', ylabel=r'$\frac{m}{s^2}$')

axs[1].plot(time, np.array(velocity), color='red')
axs[1].set(title='Velocity2',
       xlabel='time (s)', ylabel=r'$\frac{m}{s}$')

axs[2].plot(time, np.array(distance), color='blue')
axs[2].set(title='Distance2',
       xlabel='time (s)', ylabel='m')

fig.tight_layout()

plt.show()
