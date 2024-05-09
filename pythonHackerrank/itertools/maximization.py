lis = [[2, 5, 4],[3, 7, 8, 9],[5, 5, 7, 8, 9, 10]]

lists = []

for l in lis:
    lists.append([x**2 for x in l])


def DFS(data, CurrSum, Smax):
    if len(data) > 1:  # not in a leaf node
        for e in data[0]:
            subTreeMax = DFS(data[1:], CurrSum + e, Smax)
            if subTreeMax > Smax:
                Smax = subTreeMax
                print(Smax)
    else:
        for e in data[0]:
            if e + CurrSum > Smax:
                Smax = e + CurrSum
                print(Smax)
    return Smax

print(lists)
print(DFS(lists, 0, 0))