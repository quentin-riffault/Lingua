import random
import numpy as np
def distrib(distribution):
	random.seed()
	L = []
	for i in range(np.size(distribution)):
		p = int(distribution[i])
		for n in range(p):
			L.append(i)
		
	random.shuffle(L)

	if len(L) < 1:
		L.append(distrib(distribution*10))

	return L[0]
	#return L[random.randint(0, len(L))]
