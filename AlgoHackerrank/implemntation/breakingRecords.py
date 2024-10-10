
import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    numHighs = 0
    numLows = 0
    for scoreNum, score in enumerate(scores):
        if scoreNum == 0:
            mi = score
            ma = score
        if score < mi:
            numLows += 1
            mi = score
        if score > ma:
            numHighs += 1
            ma = score
    return [numHighs, numLows]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
