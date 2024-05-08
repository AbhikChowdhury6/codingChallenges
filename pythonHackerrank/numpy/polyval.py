import numpy as np

p = np.poly1d(list(map(float, input().split())))

x = float(input())

print(np.polyval(p, x))

