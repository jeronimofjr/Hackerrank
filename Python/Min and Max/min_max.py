import numpy as np 

l, c = [int(i) for i in input().split()]

array = np.array([input().split() for i in range(l)], dtype=int)

print(np.max(np.min(array, axis=1)))