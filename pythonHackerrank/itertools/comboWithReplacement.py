from itertools import combinations_with_replacement as cwr

inp = input().split()
word, k = inp[0], int(inp[1])


print("\n".join(sorted(["".join(sorted(x)) for x in list(cwr(word, k))])))
