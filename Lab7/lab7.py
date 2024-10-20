import random
import math

random.seed(42)

delta = 1.96

def get_im(m):

	sum = 0
	
	values = []

	for i in range(m):
	
		u = random.uniform(0, 1)
		
		yi = (math.exp(math.sqrt(u)) + math.exp(math.sqrt(1 - u)))/2
		
		values.append(yi)
		
		sum += yi
		
	mu = sum/m
	
	snsq = 0
	
	for i in range(m):
	
		snsq += (values[i] - mu) ** 2
		
	snsq /= (m - 1)
	
	ci_low = mu - (delta * math.sqrt(snsq))/math.sqrt(m)
	
	ci_high = mu + (delta * math.sqrt(snsq))/math.sqrt(m)
	
	return round(mu, 5), (round(ci_low, 5), round(ci_high, 5))
		
	
	

M = [50, 100, 500, 1000, 5000, 10000, 50000, 100000]

for m in M:

	mean, interval = get_im(m)

	print(f"for m = {m}, mean = {mean} and confidence interval = {interval}")
		
		
		
