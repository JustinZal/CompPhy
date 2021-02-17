import numpy as np
import matplotlib.pyplot as plt
from time import localtime
from random import random, seed


def get_seed():
    year, month, day, hour, minute, sec, _, _, _ = localtime()

    return year + 70 * (hour + 12 * (day + 31 * (day + 23 * minute + 59 * sec)))


def lc_generator(a, c, m, n, seed=None):
    if n < 0:
        return False

    if n == 0:
        return np.array([])

    I = [get_seed() if seed is None else seed]

    if n == 1:
        return np.array([I[0] / m])

    for i in range(n - 1):
        previous = I[i]
        rand_number = (a * previous + c) % m
        I.append(rand_number)

    return np.array([rand_nr / m for rand_nr in I])


def get_moment(arr, k):
    return np.power(arr, k).sum() / len(arr)

#Task 1a a)

a_1 = 25214903917
m_1 = 2 ** 48
c_1 = 11

# print('First list of random numbers:', lc_generator(a_1, c_1, m_1, 22))

#Task 1a b)

a_2 = 57
c_2 = 1
m_2 = 256
r_1_1 = 1

random_list_custom = lc_generator(a_2, c_2, m_2, 30, r_1_1)

seed(None)
random_list_python = np.array([random() for x in range(30)])
i = np.linspace(1, 30, 30)

fig, axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot(i, random_list_custom, 'bo')
axes[0].set_title('Custom Random Numbers')
axes[0].set_xlabel('ith number')
axes[0].set_ylabel('Number value')

axes[1].plot(i, random_list_python, 'ro')
axes[1].set_xlabel('ith number')
axes[1].set_ylabel('Number value')
axes[1].set_title('Python Random Numbers')
fig.tight_layout()

plt.savefig('./Test1.pdf')
plt.clf()

##Performing second test

custom_random_sublist = random_list_custom[0::2]
python_random_sublist = random_list_python[0::2]
i = np.linspace(1, 30, 15)

fig, axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot(i, custom_random_sublist, 'bo')
axes[0].set_title('Custom Random Numbers')
axes[0].set_xlabel('ith number')
axes[0].set_ylabel('Number value')

axes[1].plot(i, python_random_sublist, 'ro')
axes[1].set_xlabel('ith number')
axes[1].set_ylabel('Number value')
axes[1].set_title('Python Random Numbers')
fig.tight_layout()

plt.savefig('./Test2.pdf')
plt.clf()

fig, axes = plt.subplots(nrows=1, ncols=2)

moment_len = np.linspace(1, 10, 10)
moments = np.array([get_moment(random_list_custom, k) for k in moment_len])
comparison_moments1 = np.array([1/(k + 1) + (1/np.sqrt(len(random_list_custom)))for k in moment_len])

python_moments = np.array([get_moment(random_list_python, k) for k in moment_len])
comparison_moments2 = np.array([1/(k + 1) + (1/np.sqrt(len(random_list_python)))for k in moment_len])


axes[0].plot(moment_len, moments, 'bo')
axes[0].plot(moment_len, comparison_moments1, 'ro')
axes[0].set_title('Custom Moments')
axes[0].set_xlabel('Moment number k')
axes[0].set_ylabel('Kth moment')
axes[0].legend(['Moments of the list', 'Asymptotic bound'])

axes[1].plot(moment_len, python_moments, 'bo')
axes[1].plot(moment_len, comparison_moments2, 'ro')
axes[1].set_title('Python Moments')
axes[1].set_xlabel('Moment number k')
axes[1].set_ylabel('Kth moment')
axes[1].legend(['Moments of the list', 'Asymptotic bound'])

fig.tight_layout()

plt.savefig('./Test3.pdf')

