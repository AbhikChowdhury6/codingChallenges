_ = input()

l = list(map(int, input().split()))

os = set()
ms = set()

for e in l:
    #print(e)
    #print(os)
    #print(ms)
    if e not in ms:
        if e in os:
            os.remove(e)
            ms.add(e)
        else:
            os.add(e)

print(os.pop())