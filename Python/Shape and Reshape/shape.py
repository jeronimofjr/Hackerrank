import numpy as np 

values = input().split()
values = np.array(list(map(int, values)))

print(values.reshape(3, 3))
