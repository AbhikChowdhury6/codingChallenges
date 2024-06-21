# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()
k = input()

m = re.search(r"{}".format(k), s)

lastStart = -1

if m is None:
    print("(-1, -1)")
else:
    for i in range(len(s)):
        m = re.search(r"{}".format(k), s[i:])
        if m is not None and m.start() + i != lastStart:
            print(f"({m.start()+i}, {m.end()+i-1})")
            lastStart = m.start() + i
            