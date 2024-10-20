import math
import random
from scipy.stats import norm

random.seed(42)

### QUESTION 1 ###

def mean_n_var(vals):

    n = len(vals)

    musum = 0

    for i in range(n):

        musum += vals[i]
    
    mu = musum/n

    vsum = 0

    for i in range(n):

        vsum += (vals[i] - mu) ** 2
    
    var = vsum/(n - 1)

    return round(mu, 5), round(var, 6)

def estimate_crude(m):

    m_sum = 0
    v_sum = 0

    values = []

    for i in range(m):

        u = random.uniform(0, 1)

        yi = math.exp(u)

        values.append(yi)

    return mean_n_var(values)

def print_estimate(m):

    m_sum = 0
    v_sum = 0

    values = []

    for i in range(m):

        u = random.uniform(0, 1)

        yi = math.exp(u)

        values.append(yi)

    return mean_n_var(values)

def estimate_antithetic(m):

    m_sum = 0
    v_sum = 0

    values = []

    for i in range(m):

        u = random.uniform(0, 1)
        
        yi = (math.exp(u) + math.exp(1 - u))/2
        
        values.append(yi)
        
        m_sum += yi
        
    mu = m_sum/m

    for i in range(m):

        v_sum += (values[i] - mu) ** 2
        
    var = v_sum/(m - 1)

    return round(mu, 5), round(var, 6)

def estimate_control(m):

    m_sum = 0
    v_sum = 0

    values = []

    for i in range(m):

        u = random.uniform(0, 1)

        yi = math.exp(u) - 6 * (3 - math.e) * (u - 0.5)

        m_sum += yi

        values.append(yi)
    
    mu = m_sum/m
    
    for i in range(m):

        v_sum += (values[i] - mu) ** 2
    
    var = v_sum/(m - 1)

    return round(mu, 5), round(var, 6)

m_vals = [10, 100, 1000, 10000, 100000]

for m in m_vals:

    c_m, c_v = estimate_crude(m)
    a_m, a_v = estimate_antithetic(m)
    co_m, co_v = estimate_control(m)

    print(f"M = {m} : Crude ({c_m}, {c_v}) ; Anti ({a_m}, {a_v}, {round((abs(a_v - c_v) * 100)/c_v, 3)}) ; Contr ({co_m}, {co_v}, {round((abs(co_v - c_v) * 100)/c_v, 3)})")


### QUESTION 2 ###

def estimate_crude_two(m):

    values = []

    for i in range(m):

        y = random.expovariate(1)
        x = random.normalvariate(y, 2)

        values.append(int(x > 1))
    
    return mean_n_var(values)



def estimate_cond_two(m):

    values = []

    for i in range(m):

        y = random.expovariate(1)

        values.append(1 - norm.cdf((1 - y)/2))
    
    return mean_n_var(values)

def estimate_anti_two(m):

    values = []

    for i in range(int(m/2)):

        u = random.uniform(0, 1)

        values.append(1 - norm.cdf((1 + math.log(u))/2))
        values.append(1 - norm.cdf((1 + math.log(1 - u))/2))

    return mean_n_var(values)

print("====")

for m in m_vals:

    c_m, c_v = estimate_crude_two(m)
    a_m, a_v = estimate_anti_two(m)
    co_m, co_v = estimate_cond_two(m)

    print(f"{m} & {c_m} & {c_v} & {a_m} & {a_v} & {round((abs(a_v - c_v) * 100)/c_v, 3)} & {co_m} & {co_v} & {round((abs(co_v - c_v) * 100)/c_v, 3)} \\\\ ")

### QUESTION 3 ###

def estimate_crude_three(m):

    values = []

    for i in range(m):

        u = random.uniform(0, 1)

        n = 0

        if(u <= 0.19):

            n = 1
        
        elif(u <= 0.45):

            n = 2
        
        elif(u <= 0.69):

            n = 3
        
        elif(u <= 0.86):

            n = 4
        
        else:

            n = 5

        r = 0

        for j in range(n):

            r_i = random.weibullvariate(3, 0.8)

            r += r_i
        
        values.append(int(r < 5))
    
    mu, var = mean_n_var(values)

    interval = (mu - 2.58 * math.sqrt(var), mu + 2.58 * math.sqrt(var))
    
    return mu, var, interval

strata_p = [0.19, 0.26, 0.24, 0.17, 0.14]

def estimate_strata(m):

    mus = []
    sigmas = []

    for i in range(5):

        values = []

        for j in range(int(m * strata_p[i])):

            r = 0

            for k in range(i + 1):

                r += random.weibullvariate(3, 0.8)

            values.append(int(r < 5))
        
        mu, sig = mean_n_var(values)

        mus.append(mu)
        sigmas.append(sig)
    
    mu_overall = 0

    for i in range(5):

        mu_overall += strata_p[i] * mus[i]
    
    var_overall = 0

    for i in range(5):

        var_overall += strata_p[i] * sigmas[i]
    
    var_overall/= m

    ci_low = mu_overall - 2.58 * math.sqrt(var_overall)
    ci_high = mu_overall + 2.58 * math.sqrt(var_overall)

    return round(mu_overall, 6), round(var_overall, 6), (round(ci_low, 6), round(ci_high, 6))

new_Ms = [100, 10000]


for m in new_Ms:

    m_c, v_c, i_c = estimate_crude_three(m)

    m, v, interval = estimate_strata(m)

    print(f"{m_c} & {v_c} & {m} & {v} & {interval} \\\\ ")



