# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

N = int(input())

lis = input().split()

k = int(input())

numA = lis.count("a")

# N choose k - (N - numA) choose k / N choose k

lennCk = len(list(combinations(lis, k)))

#print(lennCk)

lenNumACk = len(list(combinations(range(N - numA), k)))


print((lennCk - lenNumACk) / lennCk)






