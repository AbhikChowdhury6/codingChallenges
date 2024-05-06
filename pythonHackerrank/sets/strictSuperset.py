A = set(list(map(int, input().split())))

n = int(input())

o = True

for _ in range(n):
    B = set(list(map(int, input().split())))
    if not (A > B):
        o = False
        break

print(o)