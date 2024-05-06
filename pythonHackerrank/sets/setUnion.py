_ = input()
s1 = set(list(map(int, input().split())))
_ = input()
s2 = set(list(map(int, input().split())))

print(len(s1.union(s2))) #this could also be written s1 | s2