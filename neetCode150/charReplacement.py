class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we have a budget of k charecters 
        # keep on reading in chars into the sublist
        # if adding the next char exceeds the budget
        # check which char has the furthest back last reference
        substr_start_i = 0
        max_len = 1
        curr_chars = {s[0]:0}
        for i in range(1, len(s)):
            curr_chars[s[i]] = i

            if len(curr_chars) > k+1:
                #find the key with the min lastSeen
                furthest_back_char = min(curr_chars, key=lambda x:curr_chars[x])
                furthest_back_char_idx = curr_chars[furthest_back_char]
                substr_start_i = furthest_back_char_idx + 1
                curr_chars.pop(furthest_back_char)
                
            len_substr = (i+1) - substr_start_i
            max_len = max(max_len, len_substr)
        
        return max_len 
            
        