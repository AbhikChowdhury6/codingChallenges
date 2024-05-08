import numpy as np

n = int(input())

al = []
for _ in range(n):
    al.append(list(map(float, input().split())))

A = np.array(al)
#print(A)

print(float(f"{np.linalg.det(A):.2f}"))