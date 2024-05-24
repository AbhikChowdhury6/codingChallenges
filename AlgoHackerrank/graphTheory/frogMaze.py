#!/bin/python3

import math
import os
import random
import re
import sys

actions = {}

class env():
    def __init__(self, tunnels, exits, mines, obsticles):
        self.tunnels = tunnels
        self.exits = exits
        self.mines = mines
        self.obsticles = obsticles
        self.seen = []
        
    def step(self, state, action):
        pass

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    # read in the board state
    exits = []
    mines = []
    obsticles = []
    state = []
    for n_itr in range(n):
        row = input()
        # Write your code here
        for colI in range(len(row)):
            if row[colI] == "#":
                obsticles.append([n_itr, colI])
            if row[colI] == "*":
                mines.append([n_itr, colI])
            if row[colI] == "%":
                exits.append([n_itr, colI])
            if row[colI] == "A":
                state = [n_itr, colI]
        
        
    # add in wall obsticles
    obsticles.extend([[-1, x] for x in range(m)])  # top wall
    obsticles.extend([[n, x] for x in range(m)])  # bottom wall
    obsticles.extend([[x, -1] for x in range(n)])  # left wall
    obsticles.extend([[x, n] for x in range(n)])  # right wall
    
    tunnels = {}
    # read in all the tunnels
    for k_itr in range(k):
        second_multiple_input = input().rstrip().split()

        i1 = int(second_multiple_input[0])

        j1 = int(second_multiple_input[1])

        i2 = int(second_multiple_input[2])

        j2 = int(second_multiple_input[3])

        # Write your code here
        tunnels[(i1, j1)] = [i2, j2]
        tunnels[(i2, j2)] = [i1, j1]

    # Write your code here
    e = env(tunnels, exits, mines, obsticles)
    
    # now it's time for the search!
    # from the current state
        # try going left
        # try going up
        # try going right
        # try going down
        # if all of them kept you in the same spot add a mine to that spot
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
