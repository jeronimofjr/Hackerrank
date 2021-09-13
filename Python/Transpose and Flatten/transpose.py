import numpy as np


# ler os valores
n, m = map(int, input().split())

# crio o array
array = np.array([list(map(int, (input().split()))) for _ in range(n)])

# printo
print(array.transpose())
print(array.flatten())