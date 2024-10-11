#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if year < 1918:  # julian leap year
        if year % 4 == 0:
            monthDays[1] += 1
    elif year > 1918:  # gregorian leap year
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            monthDays[1] += 1
    else:
        monthDays[1] += 1 - 14  # gained a day for the leap year but lost 14 for switch
    
    monthNum=0
    monthsTotal=0
    while monthsTotal + monthDays[monthNum] < 256:
        monthsTotal+= monthDays[monthNum]
        monthNum+=1
    
    return f"{256 - monthsTotal:02}.{monthNum+1:02}.{year}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
