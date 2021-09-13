import numpy as np 

np.set_printoptions(sign= ' ')

x = list(map(float, input().split()))

print(np.floor(x), np.ceil(x), np.rint(x), sep='\n')
