#from collections import Counter

def minion_game(string):
    # your code goes here
    vowels = ["A", "E", "I", "O", "U"]
    #vCountsDict = {}
    #cCountsDict = []
    cScore = 0
    vScore = 0
    sl = len(string)
    for i in range(sl):  # iterate over every posible word length
        if string[i] in vowels:
            vScore += sl-i
        else:
            cScore += sl-i
        # generate all words of length i
        #vCountsDict[i] = Counter()
        #cCountsDict[i] = Counter()
        #for j in range(len(string) - i):  # iterate over every position in the string an i length word can fit
            #print(string[j:j+i])
            #if string[j] in vowels:  # if the first letter is a vowel
                #vCountsDict[i][string[j:j+i]] += 1  # add the word to the counter
            #    vScore += 1
            #else:
                #cCountsDict[i][string[j:j+i]] += 1
            #    cScore += 1
        
        #if string[i] in vowels:
        #    VScore += 1
        #else:
        #    cScore += 1
    if vScore > cScore:
        print(f"Kevin {vScore}")
    elif vScore < cScore:
        print(f"Stuart {cScore}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)