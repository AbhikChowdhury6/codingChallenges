# it would have been faster to actually read the problem statement
# then I would have seen that we should have stopped at non nums
# we also could have seen the + and the - and the free space being easy to handle
# the cases I ended up using does seem pretty minimal
# yeah takeaway, tackle requirements section by section


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
        #s = s.strip()
        i = 0
        while i < len(s) and s[i].isnumeric():
            newS.append(s[i])
            i += 1
        if len(newS) == 0 or (len(newS) == 1 and (newS[0] == '-' or newS[0] == '+')): return 0
        i = int("".join(newS))
        i = min(i, 2**31-1)
        i = max(i, -2**31) 
        return i
        
        