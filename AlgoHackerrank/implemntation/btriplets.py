def beautifulTriplets(d, arr):
    # Write your code here
    numTriplets = 0
    # iterate over the list
    for potFirsti in range(len(arr)):
        # iterate over the rest of the list
        for potSecondi in range(potFirsti, len(arr)):
            # if the pair is a potentail triplet
            if arr[potSecondi] - arr[potFirsti] == d:
                # look for the third
                for potThirdi in range(potSecondi, len(arr)):
                    # if it's there then add the triplet
                    if arr[potThirdi] - arr[potSecondi] == d:
                        numTriplets += 1
    return numTriplets


def foundcomp(potentiali, arr, d):
    # iterate over the rest of the list
    for potNexti in range(potentiali, len(arr)):
        # if the pair is a potentail triplet
        if arr[potNexti] - arr[potentiali] == d:
            return potNexti
    
    return -1
            


def beautifulTriplets(d, arr):
    # Write your code here
    numTriplets = 0
    # iterate over the list
    for potFirsti in range(len(arr)):
        #see if there is a second
        potSecondi = foundcomp(potFirsti, arr, d)
        #if there wasn't continue
        if potSecondi < 0:
            continue
        #see if there's a third
        if foundcomp(potSecondi, arr, d) >= 0:
            numTriplets +=1
    
    return numTriplets