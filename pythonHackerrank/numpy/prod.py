import numpy as np

N, M = map(int, input().split())

A = np.array([list(map(int, input().split())) for _ in range(N)])

print(np.prod(np.sum(A, axis=0)))
