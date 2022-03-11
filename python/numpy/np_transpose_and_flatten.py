import numpy as np
N, M = (map(int, input().split()))
new_array = (np.array([input().split() for n in range(N)], dtype=int)).reshape(N, M)
print(np.transpose(new_array))
print(new_array.flatten())
