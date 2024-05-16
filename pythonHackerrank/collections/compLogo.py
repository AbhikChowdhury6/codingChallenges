#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    s = input()
    c = Counter([*s])
    zc = list(zip([x for x in c], [c[x] for x in c]))
    zc.sort(key = lambda x: (-x[1], ord(x[0]))) # sort by decending counts and then letter
    
    print("\n".join([" ".join([t[0], str(t[1])]) for t in zc[:3]]))
    
