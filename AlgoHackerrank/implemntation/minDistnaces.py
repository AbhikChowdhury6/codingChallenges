#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    arraySet = set(a)
    
    mins = []
    for item in arraySet:
        indexes = [x for x in range(len(a)) if a[x] == item]
        
        diffs = [indexes[i + 1] - indexes[i]
                 for i in range(len(indexes) - 1)]
        
        if len(diffs) > 0:
            mins.append(min(diffs))

    return -1 if len(mins) == 0 else min(mins)
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
