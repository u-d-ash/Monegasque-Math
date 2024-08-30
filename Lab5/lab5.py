import plotly.express as px
import pandas as pd
import random
import math

random.seed(42)

def box_muller():

    u1 = random.uniform(0, 1)
    u2 = random.uniform(0, 1)
    

    r = math.sqrt(-2 * math.log(u1))

    theta = 2 * math.pi * u2

    z1 = r * math.cos(theta)
    z2 = r * math.sin(theta)

    return (z1, z2)


# rho is the only variable changing in the given task, hence the method argument

mu1 = 5
mu2 = 8
sig1 = 3
sig2 = 2

def generate_bivariate(rho):

    z1, z2 = box_muller()
    
    x1 = mu1 + sig1 * z1
    x2 = mu2 + rho * sig2 * z2 + math.sqrt(1 - rho ** 2) * sig2 * z2
    
    return x1, x2

def func(x, rho):

    return mu2 + rho * (sig2/sig1) * (x - mu1)
    
    
arre = [-1, -0.5, 0, 0.5, 1]

dataframes = []


for a in arre:

    x = []
    y = []
    
    if(a == -1 or a == 1):
    
        
        for i in range(5000):
        
            x1_one, x1_two = box_muller()
            
            y1_one = func(x1_one, a)
            y1_two = func(x1_two, a)
            
            x.append(x1_one)
            y.append(y1_one)
            
            x.append(x1_two)
            y.append(y1_two)

    else:

        for i in range(10000):
        
            x1, x2 = generate_bivariate(a)
               
            x.append(x1)
            y.append(x2)

    
    thedict = {"x1" : x, "x2" : y}
    
    thedf = pd.DataFrame(thedict)
    
    dataframes.append(thedf)
     

for i, adf in enumerate(dataframes):

    tit = f"a = {arre[i]}"

    fig = px.density_heatmap(adf, x = "x1", y = "x2", title = tit)
    
    fig.show()    

for i, adf in enumerate(dataframes):

    tit = f"a = {arre[i]}"
    
    fig = px.density_contour(adf, x = "x1", y = "x2", title = tit)
    
    fig.show()


    
        
    
        
    
