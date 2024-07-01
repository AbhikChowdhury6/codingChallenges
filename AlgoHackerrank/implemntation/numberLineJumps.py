#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    # convex problem
    # take one step and see if their closer
    # if they are is the distance they got closer a multiple of their starting offset
    
    # clac the starting offset
    offset = x1 - x2
    # calc the relative motion each turn
    rmotion = v1 - v2
    # if offset/rmotion is a positive integer then yes
    return "YES" if rmotion > 0 and offset/rmotion <= 0 and (offset/rmotion).is_integer() else "NO"
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
