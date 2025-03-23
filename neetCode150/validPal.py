class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanatized = [x.lower() for x in s if x.isalnum()]
        print(sanatized)
        
        split_i = len(sanatized)//2

        first_half = sanatized[:split_i]
        print(first_half)
        
        if len(sanatized) % 2 == 0:
            rev_second_half = sanatized[-1:split_i-1:-1]
        else:
            rev_second_half = sanatized[-1:split_i:-1]
        print(rev_second_half)
        
        return first_half == rev_second_half
        