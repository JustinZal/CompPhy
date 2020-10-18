import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


GRID_SIZE = 40
ERROR = 0.001

#Setting up right side boundary condition
def copy_right_side(grid):
    for i in range(GRID_SIZE):
        grid[i, -1] = grid[i, -2]

    return grid


def get_initial_potential_grid():
    grid = np.zeros((GRID_SIZE, GRID_SIZE))

    #Setup initial boundary conditions
    grid[0, :] = 100
    grid[:, 0] = 0
    grid[-1, :] = 0

    return copy_right_side(grid)


def get_error(new_grid, ref_grid):
    return np.sum(abs(new_grid - ref_grid))


#Generate data for plotting
def generate_plotting_dataset(X, Y, S):
    Z = []

    for i in range(GRID_SIZE):
        temp = []
        for j in range(GRID_SIZE):
            temp.append(S[i, j])
        Z.append(temp)

    return np.array(Z)


def jacobi_solution(grid):
    x_len, y_len = grid.shape

    ref_grid = grid.copy()
    new_grid = grid.copy()

    #Start iterations
    while True:
        for i in range(1, x_len - 1):
            for j in range(1, y_len - 1):
                #Get neighbor values for averaging
                n1 = ref_grid[i + 1, j]
                n2 = ref_grid[i - 1, j]
                n3 = ref_grid[i, j + 1]
                n4 = ref_grid[i, j - 1]
                new_val = sum([n1,n2,n3,n4]) / 4

                new_grid[i, j] = new_val

        #Calculate error
        error = get_error(ref_grid, new_grid)
        print('Convergence error:', error)

        #Check convergence condition
        converged = (error < ERROR)

        #Set iteration variables for next iteration
        new_grid = copy_right_side(new_grid)
        ref_grid = new_grid.copy()

        if converged:
            break

    return ref_grid


def gauss_jacobi_solution(grid):
    x_len, y_len = grid.shape

    ref_grid = grid.copy()
    new_grid = grid.copy()

    while True:
        for i in range(1, x_len - 1):
            for j in range(1, y_len - 1):

                #Get neighbor values for averaging
                n1 = ref_grid[i + 1, j]
                n2 = new_grid[i - 1, j]
                n3 = ref_grid[i, j + 1]
                n4 = new_grid[i, j - 1]
                new_val = sum([n1,n2,n3,n4]) / 4

                new_grid[i, j] = new_val

        error = get_error(ref_grid, new_grid)
        print('Convergence error:', error)

        converged = (error < ERROR)

        new_grid = copy_right_side(new_grid)
        ref_grid = new_grid.copy()

        if converged:
            break

    return ref_grid


def sor_solution(grid):
    x_len, y_len = grid.shape

    ref_grid = grid.copy()
    new_grid = grid.copy()
    omega = 2/(1 + np.pi/GRID_SIZE)

    while True:
        for i in range(1, x_len - 1):
            for j in range(1, y_len - 1):
                n1 = ref_grid[i + 1, j]
                n2 = new_grid[i - 1, j]
                n3 = ref_grid[i, j + 1]
                n4 = new_grid[i, j - 1]

                #Average neighbor values + the omega coeficients
                new_val = (1 - omega) * ref_grid[i, j] + omega * sum([n1,n2,n3,n4]) / 4

                new_grid[i, j] = new_val

        error = get_error(ref_grid, new_grid)
        print('Convergence error:', error)

        converged = (error < ERROR)

        new_grid = copy_right_side(new_grid)
        ref_grid = new_grid.copy()

        if converged:
            break

    return ref_grid


#Example plotting
grid = get_initial_potential_grid()
sor = sor_solution(grid)
fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(0, 1, 1 / GRID_SIZE)
Y = np.arange(0, 1, 1 / GRID_SIZE)
X, Y = np.meshgrid(X, Y)
Z = generate_plotting_dataset(X, Y, sor)

surf = ax.plot_surface(X, Y, Z)
plt.title('SOR method')

ax.set_xlabel('X [m]')
ax.set_ylabel('Y [m]')
ax.set_zlabel('Z [V]')

plt.savefig('./SORMethod.pdf')
