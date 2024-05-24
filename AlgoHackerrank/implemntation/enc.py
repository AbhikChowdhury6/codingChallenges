#!/bin/python3

import math
import os
import random
import re
import sys
import math

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    ns = "".join(s.split())  # remove spaces
    sqrtL = math.sqrt(len(ns))  # get float sqrt
    r, c = math.floor(sqrtL), math.ceil(sqrtL) #calc row and column numbers
    sl = [ns[c*i:c*(i+1)] for i in range(math.ceil(len(s)/c))] #slice string
    el = ["".join([x[i] for x in sl if i < len(x)]) for i in range(c)]  # create the new words
    return " ".join(el)  # join them with spaces

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
