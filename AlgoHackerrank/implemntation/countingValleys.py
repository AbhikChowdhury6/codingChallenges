#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    elevations = []
    elevation = 0
    for step in path:
        elevations.append(elevation)
        if step == 'U':
            elevation += 1
        if step == 'D':
            elevation -= 1
    elevations.append(elevation)
    pathListWZeroes = []
    print(elevations)
    for e in elevations:
        if e > 0:
            pathListWZeroes.append('h')
        elif e < 0:
            pathListWZeroes.append('v')
        else:
            pathListWZeroes.append('0')
    print("".join(pathListWZeroes))
    #split by zero
    splits = "".join(pathListWZeroes).split('0')
    numValleys = 0
    for splitNum, p in enumerate(splits):
        if splitNum < len(splits) - 1:
            if len(p) > 0 and p[0] == 'v':
                numValleys += 1
    
    return numValleys
    
    
    
    
        

if __name__ == '__main__':
    path = "UUDDDUUD"
    steps = 0

    result = countingValleys(steps, path)
