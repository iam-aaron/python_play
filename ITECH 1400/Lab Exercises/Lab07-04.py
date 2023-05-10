from matplotlib.pyplot import plot, show, title
from math import sin, cos

number_of_values = 100000
# Calculate a step value for each set of x and y values.
# Note: The value 5.0 is related to the number of ‘nodes’ you’ll see in the graph – try changing this value when it’s working!

x = [0] * number_of_values
y = [0] * number_of_values

for index in range(number_of_values):
    step = float(index / number_of_values) * 5.0 * 3.14159
    x[index] = step - 1.6 * cos(24 * step)
    y[index] = step - 1.6 * sin(25 * step)



title("Graph Plot")
plot(x, y)
show() # Display plot