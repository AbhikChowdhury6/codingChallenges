def lengthOfLongestSubstring(s: str) -> int:
    #keep adding to a set and reset at the index of the repeated letter everytime you encounter one
    if len(s) == 0: return 0
    candidate_start = 0
    curr_index = 0
    max_len = 1
    for i in range(0, len(s) - 1):
        print(f"candidate_start: {candidate_start}")
        sublist = s[candidate_start:i + 1]
        print(sublist)
        if s[i+1] in sublist:
            candidate_start += sublist.find(s[i+1]) + 1
        elif max_len < len(sublist) + 1:
                max_len = len(sublist) + 1

    
    return max_len


print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("dvdf"))
#dvdf