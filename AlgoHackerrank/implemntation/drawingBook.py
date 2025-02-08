import math

def pageCount(n, p):
    # Write your code here


    return min([p//2, n//2 - p//2])


    # if p <= n//2:
    #     startPage = 1
    # else:
    #     startPage = n + 1
    # print(startPage)
    
    # distanceToStart = abs(startPage - p)
    # print(distanceToStart)

    # turns = math.ceil(distanceToStart / 2)
    # print(turns)

    # if n%2 == 1 and startPage == n + 1 and turns > 0: turns -= 1
    

    # return turns


print(pageCount(83246, 78132))