#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    # iterate over the range
    nums = []
    for i in range(p, q + 1):
        #print("***************")
        #print(i)
        d = int(math.log10(i)) + 1
        #print(d)
        right = int(str(i**2)[-d:])
        #print(right)
        left = int(str(i**2)[:-d] or 0)
        #print(left)
        
        if (i == right + left):
            nums.append(i)
    if len(nums) > 0:
        print(" ".join([str(x) for x in nums]))
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
