import math
import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(42)

nos = [10, 100, 1000, 10000, 100000, 1000000]

def CDF(X):

    sorted_X = sorted(X)

    y_vals = np.arange(1, len(sorted_X) + 1) / len(sorted_X)

    return sorted_X, y_vals


def mean_n_variance(X):

    xbar = 0

    for val in X:

        xbar += val
    
    xbar /= len(X)

    var = 0

    for val in X:

        var += ((val - xbar) ** 2)
    
    var /= len(X)

    return xbar, var

def F_inv1(x):

    return -1 * ((1 - x) ** (1/3)) + 1

fig, ax = plt.subplots(2, 3, figsize = (11.25, 7.5))

fig.suptitle("Question 1")

for t, N in enumerate(nos):

    X = []

    for i in range(N):

        randint = random.uniform(0, 1)
        X.append(F_inv1(randint))
    
    xv, yv = CDF(X)

    ax[t // 3, t % 3].step(xv, yv, where = 'post')
    ax[t // 3, t % 3].set_title(f"N = {N}")

    avg, var = mean_n_variance(X)

    print(f"N : {N}, mean : {round(avg, 5)}, var : {round(var, 5)}")

plt.show()


#2

fig, ax = plt.subplots(2, 3, figsize = (11.25, 7.5))

fig.suptitle("Question 2")

def finv_a(x):

    if(x == 1):
        return 0

    return -1 * math.log(1 - x)

def finv_b(x):

    if(x == 1):
        return 0

    return 0.5 * (1 - math.log(1 - x))

# only defined for x >= 0

def F_inv(x):

    if(x <= (1 - math.exp(-1))):

        return finv_a(x)
    
    else:

        return finv_b(x)
    
for t, N in enumerate(nos):

    X = []

    for i in range(N):

        randint = random.uniform(0, 1)

        X.append(F_inv(randint))
    
    xv, yv = CDF(X)

    ax[t // 3, t % 3].step(xv, yv, where = 'post')
    ax[t // 3, t % 3].set_title(f"N = {N}")

    avg, var = mean_n_variance(X)

    print(f"N : {N}, mean : {round(avg, 5)}, var : {round(var, 5)}")

plt.show()

#3

given_array = [2 * (i + 1) - 1 for i in range(5000)]

frequency = [0] * 5000

for i in range(pow(10, 5)):

    randint = random.uniform(0, 1)

    index = math.floor(5000 * randint)

    frequency[index] += 1

with open("frequencies.csv", "w") as f:

    f.write(f"Term, Frequency\n")

    for i in range(5000):

        f.write(f"{given_array[i]},{frequency[i]}\n")

    