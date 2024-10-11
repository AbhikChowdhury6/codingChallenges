import math

def mask(groupNum, s):
    groupMasks = [
        [1, 0, 0, 1, 0, 0, 1, 0, 0],  # 0
        [0, 1, 0, 0, 1, 0, 0, 1, 0],  # 1
        [0, 0, 1, 0, 0, 1, 0, 0, 1],  # 2
        [1, 1, 1, 0, 0, 0, 0, 0, 0],  # 3
        [0, 0, 0, 1, 1, 1, 0, 0, 0],  # 4
        [0, 0, 0, 0, 0, 0, 1, 1, 1],  # 5
        [1, 0, 0, 0, 1, 0, 0, 0, 1],  # 6
        [0, 0, 1, 0, 1, 0, 1, 0, 0]   # 7
    ]
    # print(s)
    # print(groupNum)
    # print(groupMasks[groupNum])
    # print([a * b for a, b in zip(groupMasks[groupNum], s)])
    
    return sum([a * b for a, b in zip(groupMasks[groupNum], s)])



def formingMagicSquare(s):
    m = [element for row in s for element in row]
    elementGroups = [
        [0, 3, 6],
        [1, 3],
        [2, 3, 7],
        [0, 4],
        [1, 4, 6, 7],
        [2, 4],
        [0, 5, 7],
        [1, 5],
        [2, 5, 6]
    ]

    targetRange = range(3, 27)
    minDistanceToTargets = {}
    # for every possible target find the min distance to it
    for target in targetRange:
        f = m
        dist = 0
        while not all([mask(gn, f) == target for gn in range(8)]):
            # tuples of the form (element, action, distance)
            elementDists = []
            for element in range(9):
                # sum up the distance from the element groups to the target
                fcopy = f
                # for +1 and -1
                m1dist = math.inf
                p1dist = math.inf
                if f[element] > 1:
                    fcopy = f
                    fcopy[element] = f[element] - 1
                    m1dist = sum([abs(mask(gn, fcopy) - target) for gn in elementGroups[element]])
                if f[element] < 27:
                    fcopy = f
                    fcopy[element] = f[element] + 1
                    p1dist = sum([abs(mask(gn, fcopy) - target) for gn in elementGroups[element]])
                
                if m1dist < p1dist:
                    elementDists.append((element, -1, m1dist))
                else:
                    elementDists.append((element, 1, p1dist))
            
            # action is the min
            minTuple = min(elementDists, key=lambda x: x[2])
            f[minTuple[0]] = f[minTuple[0]] + minTuple[1]
            dist += 1
        
        minDistanceToTargets[target] = dist

if __name__ == '__main__':

    s = [[4,9,2], [3,5,7], [8,1,5]]

 

    result = formingMagicSquare(s)

    print(result)