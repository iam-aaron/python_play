from matplotlib.pyplot import plot, show
import random as rnd

x_values = range(0,10)
y_values = [rnd.randint(0,100) for i in x_values]
plot(x_values, y_values)
show()


