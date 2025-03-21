from icecream import ic

def expand(s, startix, endidx):
    #check if start
    while s[startix] == s[endidx]:
        startix -= 1
        endidx += 1
        if startix == -1 or endidx == len(s):
            break
    startix += 1
    endidx -= 1
    
    #ic(startix, endidx, s[startix:endidx + 1])
    return s[startix:endidx + 1]

def lps(s):
    if len(s) == 1 or len(s) == 0:
        return s
    max_len = 1
    a_max_string = s[0]
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            continue

        this_max_palindone = expand(s, i, i+1)
        if len(this_max_palindone) > max_len:
            a_max_string = this_max_palindone
            max_len = len(this_max_palindone)
        
    for i in range(len(s)-2):
        if s[i] != s[i+2]:
            continue
        this_max_palindone = expand(s, i, i+2)
        if len(this_max_palindone) > max_len:
            a_max_string = this_max_palindone
            max_len = len(this_max_palindone)
    
    return a_max_string

print(lps("bb"))