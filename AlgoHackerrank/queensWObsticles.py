#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def obstructs(rq, cq, ro, co, D):
    if ro == rq:
        #E or W
        if co > cq:
            D["E"] = min(D["E"], (co - cq) - 1)
        else:
            D["W"] = min(D["W"], (cq - co) - 1)
    if co == cq:
        #N or S
        if ro > rq:
            D["N"] = min(D["N"], (ro - rq) - 1)
        else:
            D["S"] = min(D["S"], (rq - ro) - 1)
    if ro + co == rq + cq:
        #SE or NW
        if ro < rq:
            D["SE"] = min(D["SE"], (rq - ro) - 1)
        else:
            D["NW"] = min(D["NW"], (ro - rq) - 1)
    if ro - co == rq - cq:
        #NE or SW
        if ro < rq:
            D["SW"] = min(D["SW"], (rq - ro) - 1)
        else:
            D["NE"] = min(D["NE"], (ro - rq) - 1)

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    #without obsicles the queen will have v and h combined being 2*(n-1)
    D = {}
    D["N"], D["S"] = n - r_q, r_q - 1
    D["E"], D["W"] = n - c_q, c_q - 1
    #diagonally the minimum for each quadrant
    D["NW"], D["NE"] = min(D["N"], D["W"]), min(D["N"], D["E"])
    D["SW"], D["SE"] = min(D["S"], D["W"]), min(D["S"], D["E"])
    
    #for each direction, iterate over all obsticles and find the closest one
    for o in obstacles:
        obstructs(r_q, c_q, o[0], o[1], D)
    
    return sum([D[i] for i in D])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
