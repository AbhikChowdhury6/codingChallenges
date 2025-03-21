def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0: return 0
    candidate_start = 0
    max_len = 1
    for i in range(len(s)-1):
        sublist = s[candidate_start:i+1]
        new_letter = s[i+1]
        if new_letter in sublist:
            candidate_start += sublist.find(new_letter) + 1
        elif max_len < len(sublist) + 1:
                max_len = len(sublist) + 1
    return max_len  


print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("dvdf"))
#dvdf