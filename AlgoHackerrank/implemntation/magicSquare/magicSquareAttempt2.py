#!/bin/python3

import math
import os
import random
import re
import sys
import itertools
#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def mask(groupNum, s):
    groupMasks = [
        [1, 0, 0, 1, 0, 0, 1, 0, 0],  # 0
        [0, 1, 0, 0, 1, 0, 0, 1, 0],  # 1
        [0, 0, 1, 0, 0, 1, 0, 0, 1],  # 2
        [1, 1, 1, 0, 0, 0, 0, 0, 0],  # 3
        [0, 0, 0, 1, 1, 1, 0, 0, 0],  # 4
        [0, 0, 0, 0, 0, 0, 1, 1, 1],  # 5
        [1, 0, 0, 0, 1, 0, 0, 0, 1],  # 6
        [0, 0, 1, 0, 1, 0, 1, 0, 0]   # 7
    ]
    return sum([a * b for a, b in zip(groupMasks[groupNum], s)])

def isMagic(sq):
    for i in range(8):
        if mask(i, sq) != 15:
            return False
    return True

def findAllMagicSquares():
    magicSquares = []
    allPossSquares = list(itertools.permutations([x for x in range(1, 10)]))
    for sq in allPossSquares:
        if isMagic(sq):
            magicSquares.append(sq)
    return magicSquares

def dist(sq1, sq2):
    return sum([abs(sq1[i] - sq2[i]) for i in range(9)])

def formingMagicSquare(s):
    allMagicSqures = findAllMagicSquares()
    fs = [element for row in s for element in row]
    return min(dist(fs, ms) for ms in allMagicSqures)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
