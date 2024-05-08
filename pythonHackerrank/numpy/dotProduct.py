import numpy as np

n = int(input())

Al = []
Bl = []

for i in range(n):
    Al.append(list(map(int, input().split())))

A = np.array(Al)
# print(A)

for i in range(n):
    Bl.append(list(map(int, input().split())))

B = np.array(Bl)
# print(B)

print(np.dot(A, B))