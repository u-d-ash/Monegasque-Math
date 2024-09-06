import math
import random

random.seed(42)

def g(x):
	
	return math.exp(math.sqrt(x))
	

def get_samples(m):

	samps = []
	
	for i in range(m):
	
		u = random.uniform(0, 1)
		
		val = g(u)
		
		samps.append(val)
	
	return samps

delta = 1.96

def mean_n_var(vals):

	sums = 0
	
	for no in vals:
	
		sums += no
	
	mean = sums/len(vals)
	
	vsum = 0
	
	for no in vals:
	
		vsum += (no - mean) ** 2
	
	var = vsum/len(vals)
	
	snsq = vsum/(len(vals) - 1)
	
	ins = mean - (delta * math.sqrt(snsq))/(math.sqrt(len(vals)))
	
	ine = mean + (delta * math.sqrt(snsq))/(math.sqrt(len(vals)))
	
	return mean, var, snsq, ins, ine
	
	

M_VALS = [100, 1000, 10000, 100000]

for m in M_VALS:

	samps = get_samples(m)
	
	mu, sig, ss, start, end = mean_n_var(samps)
	
	print(f"priM = {m}, mean = {round(mu, 5)}, variance = {round(sig, 5)}, snsq = {round(ss, 5)}, interval = ({round(start, 5)}, {round(end, 5)})\n")
	
