numTestCases = int(input())
for _ in range(numTestCases):
    _ = input()
    A = set(list(map(int, input().split())))
    _ = input()
    B = set(list(map(int, input().split())))
    print(A.issubset(B)) 