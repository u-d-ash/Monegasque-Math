# YW9wel93eXZtX3pianJ6
# >:(
import random
import numpy as np
import math
random.seed(42)
import matplotlib.pyplot as plt

# Q1

def f(x):

    return 20 * x * ((1 - x) ** 3)

def g(x):

    return 1

def mean(A):

    if(len(A) == 0):
        return 0

    tot = 0

    for v in A:

        tot += v
    
    return (tot/len(A))

def variance(A):

    if(len(A) == 0):
        return 0

    x_bar = mean(A)

    tot = 0

    for val in A:

        tot += (val - x_bar) ** 2
    
    return tot/len(A)



def accrej1(c):

    itrs = 0

    while(True):

        x = random.uniform(0, 1)
        u = random.uniform(0, 1)

        expr = f(x)/(c * g(x))

        itrs += 1

        if(u <= expr):

            return x, itrs

values = []
itercounts = []

probcounter = 0

for i in range(10000):

    val, iters = accrej1(20) # Change this value to 40 for section (f)

    values.append(val)
    itercounts.append(iters)

    if(val >= 0.25 and val <= 0.75):

        probcounter+= 1

print(f"Average iterations : {round(mean(itercounts), 5)}")
print(f"Experimental Expectation : {round(mean(values), 5)}")
print(f"Experimental Probability : {round(probcounter/10000, 5)}") # 0.25 <= X <= 0.75

x = np.linspace(0, 1, 100)

fig, ax = plt.subplots()
ax.plot(x, f(x), color = 'red')        
ax2 = ax.twinx()                  
ax2.hist(values, bins = 100, color = 'blue')       

plt.show()

#2

def g(x, alpha):

    return x ** (alpha - 1)

def G_inv(x, alpha):

    return (alpha * x) * (1/alpha)

def f(x, k_alpha, alpha):

    return k_alpha * (x ** (alpha - 1)) * math.exp(-x)

def get_sample(c, a, k):

    while(True):

        xr = random.uniform(0, 1)
        x = G_inv(xr, a)

        u = random.uniform(0, 1)

        if(u <= f(x, k, a)/(c * g(x, a))):

            return x

samples = []

for i in range(10000):

    samp = get_sample(2, 0.7, 1.01208)

    samples.append(samp)

print(f"(a) Mean : {round(mean(samples), 5)}, Variance : {round(variance(samples), 5)}")


samples = []

for i in range(10000):

    samp = get_sample(7, 3, math.exp(1)/(2 * math.exp(1) - 5))

    samples.append(samp)

print(f"(b) Mean : {round(mean(samples), 5)}, Variance : {round(variance(samples), 5)}")

samples = []

for i in range(10000):

    samp = get_sample(9, 3.7, 8.00461)

    samples.append(samp)

print(f"(c) Mean : {round(mean(samples), 5)}, Variance : {round(variance(samples), 5)}")










