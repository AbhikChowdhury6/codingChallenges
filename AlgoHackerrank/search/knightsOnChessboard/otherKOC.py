import itertools

def findMin(n, i, j):
    visited = [[False for i in range(n)] for j in range(n)]
    visited[0][0] = True
    q = [(0, 0, 0)]
    moves = list(itertools.product((-i, i), (-j, j)))
    if i != j:
        moves.extend(list(itertools.product((-j, j), (-i, i))))
    while q:
        x0, y0, dist = q.pop()
        for move in moves:
            x1 = x0 + move[0]
            y1 = y0 + move[1]
            if 0 <= x1 <= n-1 and 0 <= y1 <= n-1 and not visited[x1][y1]:
                if x1 == n-1 and y1 == n-1:
                    return dist+1
                visited[x1][y1] = True
                q.insert(0, (x1, y1, dist+1))
    return -1

def knightlOnAChessboard(n):
    ans = [[0 for i in range(n-1)] for j in range(n-1)]
    for i in range(1, n):
        for j in range(i, n):
            ij_min = findMin(n, i, j)
            ans[i-1][j-1] = ij_min
            ans[j-1][i-1] = ij_min
    return ans



if __name__ == '__main__':

    n = 25  # int(input().strip())

    result = knightlOnAChessboard(n)
    
    [print(" ".join([f"{r:>2d}" for r in rn])) for rn in result]
    #print(result)
