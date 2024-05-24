from itertools import permutations
import os

print(os.getcwd())

#w = "1234567899"

#w = "1432"  # 2134

#w = "1342"  # 1423

#w = "654321"  # not possible

#w = "15432"  #21345

# w = "15342"  #15423

#w = "14532"  #15234

#w = "dkhc"

#allPoss = list(dict.fromkeys(
#            sorted(
#                ["".join(j) for j in list(permutations(w))]
#                )
#            ))

#print(allPoss)

#windex = allPoss.index(w)

#print(allPoss[windex + 1]) if windex + 1 < len(allPoss) else print("not possible")
w = "zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgwm"
w = "zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgwm"
w = "zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgmw"

#if len 1 the not possible
def big(w):
    if len(w) == 1:
        return "no answer"
    
    toSort = [w[-1]]
    #iterate through word indexes pairwize from the left
    for letterIndex in range(len(w)-2, -1, -1):
        toMove = w[letterIndex]
        toSort.append(toMove)
        if ord(w[letterIndex]) < ord(w[letterIndex + 1]):
            toSort.sort(key=ord)

            #search for the next highest letter that isn't itself
            for li in range(len(toSort)):
                if ord(toSort[li]) > ord(toMove):
                    pivotLetter = toSort.pop(li)
                    break

            word = w[:letterIndex] + pivotLetter + "".join(toSort)
            return word
    return "no answer"    

in_file = open("/home/chowder/Documents/AiLearning/codingChallenges/AlgoHackerrank/biggerIsGreater/testInp1.txt", "r") 
ou_file = open("/home/chowder/Documents/AiLearning/codingChallenges/AlgoHackerrank/biggerIsGreater/testOut1.txt", "r") 

inList = in_file.read().split("\n")
inList.pop(0)
ouList = ou_file.read().split("\n")
#make a list of testcase lines
numFailed = 0
for i in range(len(inList)):
    if big(inList[i]) != ouList[i]:
        numFailed += 1
        print("input was, we output, expected")
        print(inList[i])
        print(big(inList[i]))
        print(ouList[i])

print(numFailed)


#for each item generate the output and see if they're the same