# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

k, M = map(int, input().split())


lists = []

for _ in range(k):
    lis = list(map(int, input().split()[1:]))
    lists.append([x**2 for x in lis])


cartP = list(product(*lists))


print(max([sum(x) % M for x in cartP]))

# cartP = lists[0]

# for lis in range(1, k):
#    cartP.extend([*list(product(cartP, lists[lis]))])




# progressive catresian products to form a big list

# get the max of the functions of the list




# # print(lists)

# Smax = 0


# def DFS(data, CurrSum, Smax, m):
#     if len(data) > 1:  # not in a leaf node
#         for e in data[0]:
#             subTreeMax = DFS(data[1:], CurrSum + e, Smax, m)
#             if subTreeMax > Smax:
#                 Smax = subTreeMax
#                 # print(Smax)
#     else:
#         for e in data[0]:  # in leaf node
#             if (e + CurrSum) % m > Smax:
#                 Smax = (e + CurrSum) % m
#                 # print(Smax)
#     return Smax

# print(DFS(lists, 0, 0))

# # for li in range(k):
# #    for ei in range(len(lists[li])):
        

