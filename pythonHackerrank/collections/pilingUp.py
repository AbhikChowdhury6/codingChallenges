# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
import math

T = int(input())

for _ in range(T):
    _ = input()
    bl = list(map(int, input().split()))
    bq = deque(bl)
    tb = math.inf
    poss = True
    while len(bq) != 0:
        # see if the ends can fit a block
        #print(bq)
        if tb >= bq[0]:
            if tb >= bq[-1] and bq[0] < bq[-1]:
                tb = bq.pop()
            else:
                tb = bq.popleft()
        else:
            poss = False
            break
    print("Yes" if poss else "No")
        