import numpy as np

dimensions = list(map(int, input().split()))

print(np.zeros(dimensions, dtype=np.int32))
print(np.ones(dimensions, dtype=np.int32))