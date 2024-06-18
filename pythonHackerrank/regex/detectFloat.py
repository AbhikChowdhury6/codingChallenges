# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

# normal float regex
# 0 or 1 + or -
# 0 or 1 numbers
# a decimal point
# 1 or more numbers


i = int(input())
for _ in range(i):
    inputStr = input()

    print(re.match(r"[+-]?[0-9]*\.[0-9]+$", inputStr) != None)