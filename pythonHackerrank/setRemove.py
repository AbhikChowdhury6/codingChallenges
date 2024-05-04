_ = int(input())

sl = list(map(int, input().split()))

sl.sort(reverse = True)

s = set(sl)

n = int(input())

#print(s)

for _ in range(n):
    inp = input().split()
    command = inp[0]
    if command == "pop":
        s.pop()
    if command == "remove":
        #print(s)
        #print(int(inp[1]))
        s.remove(int(inp[1]))
    if command == "discard":
        s.discard(int(inp[1]))

print(sum(s))