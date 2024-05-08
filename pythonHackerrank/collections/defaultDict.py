from collections import defaultdict
inp = list(map(int, input().split()))

A = []
for _ in range(inp[0]):
    A.append(input())

B = []
for _ in range(inp[1]):
    B.append(input())

for b in B:
    ab = []
    for ai in range(len(A)):
        if A[ai] == b:
            ab.append(str(ai+1))
    if len(ab) == 0:
        print(-1)
    else:
        print(" ".join(ab))


#another solution
#first of all I like the map to variable syntax
m,n = map(int, input().split())
a = defaultdict(list)
#modifird the range so there was no need to update the addd index
for i in range(1, n+1):
    #I like taking in the input directly into the key
    a[input()].append(i)
for _ in range(m):
    #using the sequential or evaluation here is handy
    print(*a[input()] or [-1])