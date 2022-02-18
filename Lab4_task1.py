from matplotlib import pyplot as plt
import numpy as np


def version1(n):
    totalSum = 0  # Version 1
    matrix = np.random.randint(10, size=(n, n))
    rowSum = [0] * n
    counter = 3  # Counts the number of statement excuted, excluding the counter updates
    for i in range(0, n):
        rowSum[i] = 0
        counter += 1
        for j in range(0, n):
            rowSum[i] = rowSum[i] + matrix[i, j]
            totalSum = totalSum + matrix[i, j]
            counter += 2
    return counter


def version2(n):
    totalSum = 0  # Version 1
    matrix = np.random.randint(10, size=(n, n))
    rowSum = [0] * n
    counter = 3  # Counts the number of statement excuted, excluding the counter updates
    for i in range(0, n, 1):
        rowSum[i] = 0
        counter += 1
        for j in range(0, n):
            rowSum[i] = rowSum[i] + matrix[i, j]
            counter += 1
        totalSum = totalSum + rowSum[i]
        counter += 1
    return counter


def simulation(n):
    steps_version1 = [0] * n
    steps_version2 = [0] * n
    for i in range(0, n):
        steps_version1[i] = version1(i)
        steps_version2[i] = version2(i)
    x = list(range(n))
    plt.plot(x, steps_version2)
    plt.plot(x, steps_version1)
    plt.grid(which='both')
    plt.xlabel('Input Size(n)')
    plt.ylabel('Number of Steps')
    plt.legend(['version2', 'version1'])
    plt.show()

simulation(50)