lis = [[2, 5, 4],[3, 7, 8, 9],[5, 5, 7, 8, 9, 10]]

lists = []

for l in lis:
    lists.append([x**2 for x in l])

def DFS(data, CurrSum, Smax):
    for e in data[0]:  #for every subnode
        if len(data) > 1:  #if it's not a leaf
            subTreeMax = DFS(data[1:], CurrSum + e, Smax)
        else:
            subTreeMax = e + CurrSum
        
        if subTreeMax > Smax: #update mz seen so far
                Smax = subTreeMax

    return Smax



print(lists)
print(DFS(lists, 0, 0))