# McKenna Branting
# Benchmark - Project 6 - Numeric Computations with Taylor Polynomials

# Packages used: time, numpy, matplotlib
import numpy as np
import matplotlib.pyplot as plt
import time

# Starting the timer to check the computational time
start = time.time()


def tayPolA(x):
    # function to determine the solution for part 1 a
    y0 = 1
    y1 = -x
    y2 = 0
    y3 = -1 / 3 * pow(x, 3)
    y4 = -1 / 12 * pow(x, 4)
    return y0 + y1 + y2 + y3 + y4


def tayPolB(x):
    # function to determine solution for part 1 b
    y0 = 6
    y1 = x - 3
    y2 = -11 / 2 * pow(x - 3, 2)
    return y0 + y1 + y2


def powerSeries(x, a0, a1):
    # function for the solution of Part 2
    a0 = a0 * (1 - (1 / 8) * pow(x, 2) + (1 / 128) * pow(x, 4) - (13 / 15360) * pow(x, 6) +
               (403 / 3440640) * pow(x, 8) - (22971 / 1238630400) * pow(x, 10))
    a1 = a1 * (x - (1 / 24) * pow(x, 3) + (7 / 1920) * pow(x, 5) - (7 / 15360) * pow(x, 7) +
               (301 / 3932160) * pow(x, 9))
    function = a0 + a1
    return function


# step size utilized
dt = 0.02
# total number of steps
num_steps = 10000

# create of the x space between -100 and 100
xs = np.linspace(-100, 100, num_steps)
# empty space for the values of Part 1a
y1a = np.empty(num_steps)
# empty space for the values of Part 1b
y1b = np.empty(num_steps)
# empty space for the values of Part 2
y2 = np.empty(num_steps)

for i in range(-5000, 5000):  # for loop to enter values into arrays
    y1a[i] = tayPolA(i * dt)  # input values for part 1a
    y1b[i] = tayPolB(i * dt)  # input values for part 1b
    y2[i] = powerSeries(i * dt, 2, 2)  # input values for part 2 with given inputs for a0 and a1

# calculates the computational times of the program

end = time.time()
print("Computing Time: ")
print(end - start, " in seconds")

# plots the graphs

# plot of graph for part 1a
plt.title("Taylor Series Part 1a")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xs, y1a)
plt.show()

# plot of graph for part 1b
plt.title("Taylor Series Part 1b")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xs, y1b)
plt.show()

# plot of graph for part 2
plt.title("Power Series Part 2")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xs, y2)
plt.show()
