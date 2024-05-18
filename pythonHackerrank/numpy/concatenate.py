import numpy as np

M1numRows, M2numRows, numCols= map(int, input().split())

matrix1 = np.array([list(map(int, input().split())) for _ in range(M1numRows)])


matrix2 = np.array([list(map(int, input().split())) for _ in range(M2numRows)])

print(np.concatenate((matrix1, matrix2), axis=0))
