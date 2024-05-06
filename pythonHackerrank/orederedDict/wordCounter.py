from collections import OrderedDict
n = int(input())

od = OrderedDict()

for _ in range(n):
    word = input()
    if word not in od:
        od[word] = 1
    else:
        od[word] += 1
        
print(len(od.items()))
print(" ".join([str(od[x]) for x in od]))