# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()
k = input()

print(re.findall(r"{}".format(k), s))
print(re.search(r"{}".format(k), s))
print(re.search(r"{}".format(k), s))