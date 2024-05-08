from collections import Counter
_ = input()
shoeCounts = Counter(list(map(int, input().split())))

nc = int(input())

money = 0

for _ in range(nc):
    ci = list(map(int, input().split()))
    if shoeCounts[ci[0]] > 0:
        shoeCounts[ci[0]] -= 1
        money += ci[1]

print(money)