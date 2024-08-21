import random
import math

def laplace_gen():

    w = 0
    x = 0

    while(True):
        u = random.randint(0, 1)
        x = -1 * math.log(u)
        w = random.randint(0, 1)

        if(2 * math.log(w) >= (math.abs(x) - 1) ** 2):

            break
    
    if(w < 0.5):

        x = -1 * x
    
    return x

def box_muller():

    u1 = random.randint(0, 1)
    u2 = random.randint(0, 1)

    r = math.sqrt(-2 * math.log(u1))

    theta = 2 * math.pi * u2

    z1 = r * math.cos(theta)
    z2 = r * math.sin(theta)

    return z1, z2

def mar_n_bay():

    u1 = 0
    u2 = 0

    while(True):

        u1 = random.randint(0, 1)
        u2 = random.randint(0, 1)

        u1 = 2 * u1 - 1
        u2 = 2 * u2 - 1

        if(u1 ** 2 + u2 ** 2 <= 1):
            break
    
    z1 = u1 * math.sqrt((-2 * math.log(u1**2 + u2**2))/(u1**2 + u2**2))

    z2 = u2 * math.sqrt((- 2 * math.log(u1**2 + u2**2))/(u1**2 + u2**2))

    return z1, z2






