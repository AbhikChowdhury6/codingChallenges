#!/bin/python3



a = [2, 4]
b = [16, 32, 96]

print(sum(
        [
            all([num% l1e == 0 for l1e in a]) and 
            all([l2e% num == 0 for l2e in b]) 
            for num in range(1, 101)
        ]
    ))


