#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
             11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'Fourteen', \
             15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
             19: 'Nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two', \
             23: 'twenty three', 24: 'twenty four', 25: 'twenty five', 26: 'twenty six', \
             27: 'twenty seven', 28: 'twenty eight', 29: 'twenty nine'}

def timeInWords(h, m):
    # Write your code here
    out = ""
    if m == 0:
        return num2words[h] + " o' clock"
    
    
    if m < 30:
        if m == 15:
            out += "quarter"
        else:
            out += num2words[m] + " minute"
            if m > 1:
                out += "s"
            
        out += " past " + num2words[h]
    
    elif m > 30:
        if m == 45:
            out += "quarter"
        else:
            out += num2words[60-m] + " minute"
            if 60 - m > 1:
                out += "s"
        
        out += " to " + num2words[h+1]
    
    else:
        out += "half past " + num2words[h]

    return out
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
