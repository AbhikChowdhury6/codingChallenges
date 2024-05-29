#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#


# update location
def ul(location, move):
    return [location[0] + move[0], location[1] + move[1]]

def isLegal(location, move, n) -> bool:
    potLoc = ul(location, move)
    if potLoc[0] > n-1 or potLoc[1] > n-1:
        return False
    if potLoc[0] < 0 or potLoc[1] < 0:
        return False
    return True

# return the beast move Index
def bestMovei(location,
              moves,
              isRow,
              n: int,
              lastMovei: int) -> int:
    # if it is optimizing for columns
    pontentialMoves = {mi: (n-1) - moves[mi][int(isRow)]
                       for mi in range(len(moves))
                       if isLegal(location, moves[mi], n)}
    
    if len(pontentialMoves) == 0:
        return -1
    
    nextMovei = min(pontentialMoves, key=lambda x: pontentialMoves[x])

    #fi the next move moves you further away, say no potential moves
    if moves[nextMovei][int(isRow)] < 0:
        return -1

    # if you undid your previous move
    if ul(moves[nextMovei], moves[lastMovei]) == [0,0]:
        return -1
    
    return min(pontentialMoves, key=lambda x: pontentialMoves[x])
    


def solveboard(i: int, j: int, n: int) -> int:
    moves = [[i, j],
             [j, i],
             [-i, j],
             [i, -j],
             [-i, -j],
             [-j, i],
             [j, -i],
             [-j, -i]]
    
    location = [0, 0]
    numMoves = 0
    pastLocations = []

    pontentialMoves = {mi: (n-1) - moves[mi][0]
                       for mi in range(len(moves))
                       if isLegal(location, moves[mi], n)}
    
    nextMovei = min(pontentialMoves, key=lambda x: pontentialMoves[x])

    location = ul(location, moves[nextMovei])
    numMoves += 1
    lastMovei = nextMovei

    while location != [n-1, n-1]:
        # optimize cols first
        while True:
            # keep executing greedy moves to get us closer to the target col
            nextMovei = bestMovei(location, moves, False, n, lastMovei)
            if nextMovei != -1:
                location = ul(location, moves[nextMovei])
                lastMovei = nextMovei
                numMoves += 1
                
            else:
                break
        
        
        # then optimize rows
        while True:
            # keep executing greedy moves to get us closer to the target col
            nextMovei = bestMovei(location, moves, True, n, lastMovei)
            if nextMovei != -1:
                location = ul(location, moves[nextMovei])
                lastMovei = nextMovei
                numMoves += 1
            else:
                break
        
        # if you're somewhere you have already been return -1
        if location in pastLocations:
            break
        else:
            pastLocations.append(location)
        
    
    else:  # sucess case for the while
        return numMoves
    
    return -1

def knightlOnAChessboard(n):
    # Write your code here
    
    for i in range(1,n):
        output = []
        for j in range(1,n):
            output.append(str(solveboard(i, j, n)))
        print(" ".join(output))

if __name__ == '__main__':

    n = 5  # int(input().strip())

    result = knightlOnAChessboard(n)

    print(result)
