# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

inp = input().split()
wordl, k = [*inp[0]], int(inp[1])

comb = []

for i in range(k):
    t = list(combinations(wordl, i+1))
    ts = ["".join(sorted(x)) for x in t]
    comb.extend(sorted(ts))



for x in comb: print(x)
