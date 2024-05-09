from itertools import permutations

inp = input().split()
wordl, k = [*inp[0]], int(inp[1])

perm = list(permutations(wordl, k))

permS = ["".join(x) for x in perm]

permS.sort()

for x in permS: print(x)