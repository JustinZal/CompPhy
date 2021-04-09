import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#Setting the colors for later plotting. Otherwise colors of the graphs match
matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=['red', 'green', 'blue', 'yellow', 'black', 'orange', 'pink', 'purple', 'lime'])

a = 1
b = 5

#Function to be integrated
def f(x):
    return (x**2 + x) * np.exp(-x)

#Probability distribution selector, basic idea is that the number is passed and according function is selected
def p(x, n):
    if x < 0:
        return 0

    #Distribution functions are normalized, by integrating from 1 to 5 and setting the result to 1 and solving for integration constant
    return [
        lambda x: 0.25,
        lambda x: (1/(np.exp(-1) - np.exp(-5)) * np.exp(-x)),
        lambda x: (1/(np.exp(-5) * (7 * np.exp(4) - 43))) * (x ** 2 + x) * np.exp(-x)
    ][n](x)


#Get candidate for the next point and enforce it to be in the integration domain
def get_candidate(x, max_step_size):
    #Draw random point
    delta = np.random.uniform(-max_step_size, max_step_size)
    x_trial = x + delta

    #while step not in integral domain repeat drawing
    while not (a <= x_trial <= b):
        delta = np.random.uniform(-max_step_size, max_step_size)
        x_trial = x + delta

    return x_trial

def get_next_point(x, max_step_size, n):
    #Get the next point
    x_trial = get_candidate(x, max_step_size)
    #Compute W, n is passed as a number to previously described distribution selection mechanism
    w = float(p(x_trial, n)) / float(p(x, n))

    if w >= 1:
        return x_trial

    return x_trial if np.random.uniform() <= w else x

#Function to collect points for computing mean
def get_points(max_step, N, n):
    points = [1]

    for i in range(N):
        next_point = get_next_point(points[i], max_step, n)
        points.append(next_point)

    return np.array(points)

#Function that actually does integration
def integrate_function(max_step, N, n):
    points = get_points(max_step, N, n)

    return sum([f(x) / p(x, n) for x in points]) / N


steps = [0.1, 0.5, 1]

for s in steps:
    for i in range(3):
        print(integrate_function(s, 10000, i), 'Results for distribution', i + 1, 'Steps', s, 'Number of samples', 10000)


#Part B

#Analytical answer of the integral. The process of integration attached in the PDF with the submission
result = lambda x: np.exp(-x) * (-x**2 - 3 * x - 3)
analytical_answer = result(5) - result(1)

#Error calculation function
def compute_error(max_step, N, n):
    numerical = integrate_function(max_step, N, n)

    return np.abs(numerical - analytical_answer)

N_sizes = [1000 * x for x in range(1, 20)]
legends = []

print('Computing errors')
for s in steps:
    for i in range(3):
        errors = [compute_error(s, N, i) for N in N_sizes]
        print(errors)
        plt.plot(N_sizes, errors)
        legends.append(f'Step size: {s}, distribution {i}')

plt.legend(legends, loc='upper right')

plt.tight_layout()
plt.xlabel('N')
plt.ylabel('Error')
plt.savefig('./Errors.pdf')

fig, axs = plt.subplots(3, 3)

#Generating histograms
for s in range(len(steps)):
    for index in range(3):
        points = get_points(steps[s], 10000, index)
        i = 0
        j = 1
        intervals = np.arange(a, b + 0.1, 0.1)
        histogram_data = []
        #Method to go through all intervals and figure out how many elements fall in range
        while j < len(intervals):
            histogram_data.append(((intervals[i] <= points) & (points <= intervals[j])).sum())
            i += 1
            j += 1

        axs[s, index].hist(np.array(histogram_data), bins='auto')
        axs[s, index].set_title(f'Step {s}, distribution {index}')

fig.tight_layout()
plt.savefig('Interval Distribution.pdf')

