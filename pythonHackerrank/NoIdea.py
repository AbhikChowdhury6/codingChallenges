n, m = map(int, input().split())

arr = list(map(int, input().split()))

A = set(list(map(int, input().split())))

B = set(list(map(int, input().split())))

happiness = 0

for e in arr:
    if e in A: happiness += 1
    if e in B: happiness -= 1

print(happiness)