if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    s1 = set(arr)
    n2 = int(input())
    arr2 = list(map(int, input().split()))
    s2 = set(arr2)
    
    sds = set()
    sds = sds.union(s1.difference(s2))
    sds = sds.union(s2.difference(s1))
    
    #print(sds)
    
    sdl = sorted(sds)
    for e in sdl:
        print(e)