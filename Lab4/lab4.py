import random
import math
import time

import matplotlib.pyplot as plt

import numpy as np

import numpy.random

random.seed(42)

def plotthis(vals):

    plt.hist(vals, bins = 100)
    
    plt.show()


def mean_n_var(vals):

    if(len(vals) == 0):
       
        return 0, 0

    tot = 0
    
    for val in vals:
    
        tot += val
       
    xbar = tot/len(vals)
    
    toto = 0
    
    for val in vals:
    
        toto += ((val - xbar) ** 2)
        
    variance = toto/len(vals)
    
    return xbar, variance

def box_muller():

    u1 = random.uniform(0, 1)
    u2 = random.uniform(0, 1)
    

    r = math.sqrt(-2 * math.log(u1))

    theta = 2 * math.pi * u2

    z1 = r * math.cos(theta)
    z2 = r * math.sin(theta)

    return (z1, z2)


def mar_n_bay():

    u1 = 0
    u2 = 0

    all_count = 0
    rej_count = 0

    while True:

        u1 = random.uniform(0, 1)
        u2 = random.uniform(0, 1)

        u1 = 2 * u1 - 1
        u2 = 2 * u2 - 1

        all_count += 1

        if u1 ** 2 + u2 ** 2 <= 1:
            break
        else:
            rej_count += 1

    z1 = u1 * math.sqrt(-2 * math.log(u1 ** 2 + u2 ** 2) / (u1 ** 2
                        + u2 ** 2))

    z2 = u2 * math.sqrt(-2 * math.log(u1 ** 2 + u2 ** 2) / (u1 ** 2
                        + u2 ** 2))

    prop = rej_count / all_count

    return (z1, z2, prop)


# box-muller method

values_100 = []

beg = time.time()

for i in range(50):

    (v1, v2) = box_muller()

    values_100.append(v1)
    values_100.append(v2)

time.sleep(1)

end = time.time()

print(f"time for boxmuller 100 vals : {round(end - beg, 5)}")

mean1, var1 = mean_n_var(values_100)

print(f"sample mean, variance for boxmuller 100 vals : ({round(mean1, 5)}, {round(var1, 5)})")

values_10000 = []

beg2 = time.time()

for i in range(5000):

    (v1, v2) = box_muller()

    values_10000.append(v1)
    values_10000.append(v2)

time.sleep(1)

end2 = time.time()

print(f"time for boxm8uller 10000 vals : {round(end2 - beg2, 5)}")

mean2, var2 = mean_n_var(values_10000)

print(f"sample mean, variance for boxmuller 10000 vals : ({round(mean2, 5)}, {round(var2, 5)})")

# marsaglia and bay

values_100_2 = []

beg3 = time.time()

prowt = 0

for i in range(50):

    (v1, v2, pro) = mar_n_bay()
    
    values_100_2.append(v1)
    values_100_2.append(v2)
    
    prowt += pro

time.sleep(1)

end3 = time.time()

print(f"time for marsaglia, bay 100 vals : {round(end3 - beg3, 5)}")

mean3, var3 = mean_n_var(values_100_2)

print(f"sample mean, variance for marsaglia 100 vals : ({round(mean3, 5)}, {round(var3, 5)})")

print(f"proportion of values rejected : {prowt/50}")


values_10000_2 = []

beg4 = time.time()

prowt = 0

for i in range(5000):

    (v1, v2, pro) = mar_n_bay()
    
    values_10000_2.append(v1)
    values_10000_2.append(v2)
    
    prowt += pro

time.sleep(1)

end4 = time.time()

print(f"time for marsaglia, bay 100 vals : {round(end4 - beg4, 5)}")

mean4, var4 = mean_n_var(values_10000_2)

print(f"sample mean, variance for marsaglia 10000 vals : ({round(mean4, 5)}, {round(var4, 5)})")

print(f"proportion of values rejected : {prowt/5000}")



boxmul_one = [5 * x for x in values_10000]
boxmul_two = [5 * (x + 1) for x in values_10000]

marble_one = [5 * x for x in values_10000_2]
marble_two = [5 * (x + 1) for x in values_10000_2]

"""
plotthis(values_100)
plotthis(values_10000)

plotthis(values_100_2)
plotthis(values_10000_2)

plotthis(boxmul_one)
plotthis(boxmul_two)

plotthis(marble_one)
plotthis(marble_two)
"""

def f(x):

    return (math.exp(-1 * (x ** 2)) / (1 + abs(x)))
    
def g(x):

    return 2 * math.exp(2 * x)

def integralfunc(c):

    while(True):

        x = np.random.exponential(0.5) # i don't know how to generate from exponential from uniform as of now, so I am using numpy. 

        u = random.uniform(0, 1)
        
        if(u <= f(x)/(c * g(x))):
        
            return x



integralvalues = []

for i in range(100000):

    val = integralfunc(math.exp(1) * 0.5)
    
    integralvalues.append(val)

n, bins, _ = plt.hist(integralvalues)

bin_widths = np.diff(bins) 
area = np.sum(n * bin_widths)

print(f"approximate integral = {area}")
    
    
    



    
    





