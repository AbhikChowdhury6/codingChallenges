class Solution:
    def isPalindrome(self, s: str) -> bool:
        start_idx = 0
        end_idx = len(s)-1
        while start_idx < end_idx:
            while not s[start_idx].isalnum() and start_idx < end_idx:
                start_idx += 1
            while not s[end_idx].isalnum() and start_idx < end_idx:
                end_idx -= 1
            
            if s[start_idx].lower() != s[end_idx].lower():
                return False
            
            start_idx += 1
            end_idx -= 1
        return True
            

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
        