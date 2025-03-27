class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        curr_max_len = 1
        sublist_cutoff = 0
        for i in range(1, len(s)):
            new_char = s[i]
            sublist = s[sublist_cutoff:i]
            if new_char in sublist:
                sublist_cutoff += sublist.index(new_char) + 1
            
            sublist_len = (i+1) - sublist_cutoff # +1 since the cutoff is after the i
            if  sublist_len > curr_max_len:
                curr_max_len = sublist_len

        return curr_max_len
        