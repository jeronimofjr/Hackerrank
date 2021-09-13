import numpy as np 

np.set_printoptions(legacy='1.13')

n, m = list(map(int, input().split()))

arr = np.array([list(map(int, input().split())) for _ in range(n)])

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.std(arr))