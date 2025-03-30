class Solution:
    def myAtoi(self, s: str) -> int:
        newS = []
        s = s.strip()
        if len(s) == 0: return 0
        if s[0] == '-':
            newS.append('-')
            s = s[1:]
        elif s[0] == '+':
            newS.append('+')
            s = s[1:]
        
        i = 0
        while i < len(s) and (s.strip()[i].isnumeric()):
            newS.append(s[i])
            i += 1
        if len(newS) == 0 or (len(newS) == 1 and (newS[0] == '-' or newS[0] == '+')): return 0
        i = int("".join(newS))
        i = min(i, 2**31-1)
        i = max(i, -2**31) 
        return i
        
        