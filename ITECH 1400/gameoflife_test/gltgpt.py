import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# set the grid size
N = 20

# initialize the grid
grid = np.zeros((N, N), dtype=int)

# set some initial conditions
grid[N//2, N//2] = 1
grid[N//2+1, N//2] = 1
grid[N//2-1, N//2] = 1
grid[N//2, N//2+1] = 1
grid[N//2, N//2-1] = 1
# grid[0, 0] = 1
# grid[0, 1] = 1
# grid[0, 2] = 1
# grid[1, 0] = 1
# grid[1, 1] = 1

# create a toroidal index function
def toroidal_index(i):
    return i % N

# create the animation function
def update(frame_number, grid, N):
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            # count the number of live neighbors
            # neighbors = (
            #     grid[toroidal_index(i-1), toroidal_index(j-1)] +
            #     grid[toroidal_index(i-1), toroidal_index(j)] +
            #     grid[toroidal_index(i-1), toroidal_index(j+1)] +
            #     grid[toroidal_index(i), toroidal_index(j-1)] +
            #     grid[toroidal_index(i), toroidal_index(j+1)] +
            #     grid[toroidal_index(i+1), toroidal_index(j-1)] +
            #     grid[toroidal_index(i+1), toroidal_index(j)] +
            #     grid[toroidal_index(i+1), toroidal_index(j+1)]
            # )
            neighbors = (grid[(i-1+N)%N][(j-1+N)%N] +
                grid[(i-1+N)%N][j] +
                grid[(i-1+N)%N][(j+1)%N] +
                grid[i%N][(j+1)%N] +
                grid[(i+1)%N][(j+1)%N] +
                grid[(i+1)%N][j] +
                grid[(i+1)%N][(j-1+N)%N] +
                grid[i][(j-1+N)%N])
            # apply the rules of the game of life
            if grid[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if neighbors == 3:
                    new_grid[i, j] = 1
    # update the grid
    grid[:] = new_grid[:]
    # update the plot
    mat.set_data(grid)
    return mat,

# create the animation
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap='binary')
ani = animation.FuncAnimation(fig, update, fargs=(grid, N), frames=100, interval=100, save_count=50)
# update(1, grid, N)
# update(1, grid, N)
# show the animation
plt.show()
