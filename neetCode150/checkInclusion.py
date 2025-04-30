
def checkInclusion(s1: str, s2: str) -> bool:
    wSize = len(s1)
    start_window = s2[:wSize]
    print(start_window)
    counts = {s:start_window.count(s) for s in set(start_window)}
    print(counts)
    targetCounts = {s:s1.count(s) for s in set(s1)}
    print(targetCounts)
    if counts == targetCounts:
        return True

    #updates the window
    for i in range(1, len(s2) - wSize + 1):
        print("curr window:", s2[i:i+wSize])
        
        new_letter = s2[i + wSize - 1]
        print(new_letter)
        if new_letter not in counts:
            counts[new_letter] = 0
        counts[new_letter] += 1

        old_letter = s2[i-1]
        print(old_letter)
        if counts[old_letter] <= 1:
            del counts[old_letter]
        else:
            counts[old_letter] -= 1
        
        print(counts)
        if counts == targetCounts:
            return True
        
    return False
        
s1 = "ab"
s2 = "lecabee"
print(checkInclusion(s1, s2))

    