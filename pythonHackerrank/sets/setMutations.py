_ = input()
s1 = set(list(map(int, input().split())))
n = int(input())

for _ in range(n):
    cmd = input().split()[0]
    fun = getattr(s1, cmd)
    #print(fun)
    fun(set(list(map(int, input().split()))))
    
print(sum(s1))