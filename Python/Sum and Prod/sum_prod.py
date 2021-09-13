import numpy as np 

n, m = list(map(int, input().split()))
print(np.array(np.array([input().split() for _ in range(n)], dtype=int).sum(axis=0)).prod())
