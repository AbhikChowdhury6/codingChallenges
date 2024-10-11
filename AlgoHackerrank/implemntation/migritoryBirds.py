#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    bird_types = sorted(list(set(arr)))
    countsDict = {btype: arr.count(btype) for btype in bird_types}
    maxSighted = max([countsDict[btype] for btype in bird_types])
    for bt in bird_types:
        if countsDict[bt] == maxSighted:
            return bt
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
