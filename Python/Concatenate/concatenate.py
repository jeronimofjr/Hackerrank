import numpy as np 

n, m, p = [ int(i) for i in input().split()]

arr1 = np.array([list(map(int, input().split())) for _ in range(n)])
arr2 = np.array([list(map(int, input().split())) for _ in range(m)])

print(np.concatenate((arr1, arr2), axis=0))

