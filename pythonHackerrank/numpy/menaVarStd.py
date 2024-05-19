import numpy as np

#np.set_printoptions(legacy="1.13")


N, M = map(int, input().split())

A = np.array([list(map(int, input().split())) for _ in range(N)])

print(np.mean(A, axis=1))
print(np.var(A, axis=0))
print(float(f"{np.std(A):.11f}"))
