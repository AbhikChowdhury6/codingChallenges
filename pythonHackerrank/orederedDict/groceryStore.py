from collections import OrderedDict

n = int(input())

od = OrderedDict()

for _ in range(n):
    inp = input().split(" ")
    k = " ".join(inp[:-1])
    if k not in od:
        od[k] = int(inp[-1])
    else:
        od[k] += int(inp[-1])
    
for i in od:
    print(f"{i} {od[i]}")