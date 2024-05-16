# Enter your code here. Read input from STDIN. Print output to STDOUT


from collections import deque

d = deque()

n = int(input())

for _ in range(n):
    inp = input().split()
    func = d.__getattribute__(inp[0])
    func(inp[1]) if len(inp) > 1 else func()

print(" ".join(list(d)))

