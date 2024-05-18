import numpy as np
numRows, numCol = map(int, input().split())

matrix = np.array([list(map(int, input().split())) for _ in range(numRows)])

print(np.transpose(matrix))

print(matrix.flatten())
