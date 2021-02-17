import numpy as np
import matplotlib.pyplot as plt
from time import localtime
from random import random, seed

#Get seed with the formula described in the class
def get_seed():
    year, month, day, hour, minute, sec, _, _, _ = localtime()

    return year + 70 * (hour + 12 * (day + 31 * (day + 23 * minute + 59 * sec)))

#Perform random number generation with LC generator
def lc_generator(a, c, m, n, seed=None):
    if n < 0:
        return False

    if n == 0:
        return np.array([])

    I = [get_seed() if seed is None else seed]

    if n == 1:
        return np.array([I[0] / m])
    #Perform sucessive iteration
    for i in range(n - 1):
        previous = I[i]
        rand_number = (a * previous + c) % m
        I.append(rand_number)

    #Perform
    return np.array([rand_nr / m for rand_nr in I])


#Funcion to get k-th moment
def get_moment(arr, k):
    return np.power(arr, k).sum() / len(arr)

#Task 1a a)

a_1 = 25214903917
m_1 = 2 ** 48
c_1 = 11

print('First list of random numbers:', lc_generator(a_1, c_1, m_1, 22))

#Task 1a b)

a_2 = 57
c_2 = 1
m_2 = 256
r_1_1 = 1

random_list_custom = lc_generator(a_2, c_2, m_2, 30, r_1_1)
#Initialize random seed
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

python_x = []
python_y = []
custom_x = []
custom_y = []
#Collect dataset for second test plots

for i in range(len(random_list_custom)):
    python_x.append(random_list_python[2 * i])
    python_y.append(random_list_python[2 * i + 1])
    custom_x.append(random_list_custom[2 * i])
    custom_y.append(random_list_custom[2 * i + 1])


    if 2 * i + 1 >= len(random_list_custom) - 1:
        break

fig, axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot(np.array(custom_x), np.array(custom_y), 'bo')
axes[0].set_title('Custom Random Numbers')
axes[0].set_xlabel('ith number')
axes[0].set_ylabel('Number value')

axes[1].plot(np.array(python_x), np.array(python_y), 'ro')
axes[1].set_xlabel('ith number')
axes[1].set_ylabel('Number value')
axes[1].set_title('Python Random Numbers')
fig.tight_layout()

plt.savefig('./Test2.pdf')
plt.clf()

fig, axes = plt.subplots(nrows=1, ncols=2)

#Get moments for comparison + analytic moments
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

#Problem 1B

#Random walk simulations and expected value computations
def simulate_walk(p_right, number_of_steps):
    return sum([1 if random() < p_right else -1 for i in range(number_of_steps)])

def simulate_squared_walk(p_right, number_of_steps):
    return sum([1 if random() < p_right else -1 for i in range(number_of_steps)]) ** 2

def get_expectation(N, p_right):
    return sum([simulate_walk(p_right, N) for i in range(100000)]) / 100000

def get_expectation_squared(N, p_right):
    return sum([simulate_walk(p_right, N) for i in range(100000)]) / 100000


p_right = 0.8
p_left = 0.2

N = [4, 8, 16, 32, 64, 128, 256]

expectations = [get_expectation(n, p_right) for n in N]
analytical_expectations = [(p_right - p_left) * n for n in N]

print('Numerical expectation of distance:', expectations)
print('Analytical expectation of distance:', analytical_expectations)

expectations_squared = [get_expectation_squared(n, p_right) for n in N]
analytical_squared_expectations = [4 * p_right * p_left * n for n in N]

print('Numerical expectation of distance squared:', expectations_squared)
print('Analytical expectation of distance squared:', analytical_squared_expectations)

plt.clf()
plt.plot(np.array(N), np.array(expectations_squared), 'o')
plt.plot(np.array(N), np.array(analytical_squared_expectations), 'o')
plt.legend(['Numerical expectation squared', 'Analytical expectation squared'])
plt.xlabel('N')
plt.ylabel('Expectation of distance squared')
plt.savefig('./ExpectationDistanceSquared.pdf')
plt.clf()

#Problem 2B

def simulate_distinct_steps(steps, p_right):
    iterations = 100000
    unique_steps = []
    # Simulation of distinct steps, simulating path, and calculating set length
    for i in range(iterations):
        set_of_steps = set({})
        position = 0
        for k in range(steps):
            set_of_steps.add(position)
            walks = [-1, 1]
            position += walks[int(p_right < random())]

        # print(set_of_steps)
        unique_steps.append(len(set_of_steps))

    return sum(unique_steps) / len(unique_steps)

#Compute distinct steps and plot dependence
steps = np.linspace(10, 100, 10)
unique_step_expectations = np.array([simulate_distinct_steps(int(s), p_right) for s in steps])

plt.plot(steps, unique_step_expectations, 'o')
plt.xlabel('Number of steps (N)')
plt.ylabel('Expected amount of unique steps')
plt.savefig('./ExpectationOfUniqueSteps.pdf')