# Enter your code here. Read input from STDIN. Print output to STDOUT

N, X = map(int, input().split())

l = []
for _ in range(X):
    l.append(list(map(float, input().split())))

print("\n".join([str(sum(x)/X) for x in zip(*l)]))

#print("\n".join([str(sum([x[i] for x in l])/X) for i in range(N)]))