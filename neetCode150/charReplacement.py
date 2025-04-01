class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #ok new plan
        # once I hit k number of different charecters reset start i 
        # move up star i until it saves me a change
        #min num of diff chars has to = k
        # intake the new char and move the start i up until you save on a switch
        #should I keep a dict of the counts of each charecter
        # and then sum the counts of every non max char
        def getMaxKey(d):
            return max(d.keys(), key = lambda x:d[x])
        
        def getNumMaxKeys(mk, d):
            return len([x for x in d if d[x] == d[mk]])
        
        def numChanges(mk, d):
            return sum(d.values()) - d[mk]
        
        substr_start_i = 0
        max_len = 1
        curr_letter_counts = {s[0]:1}
        for i in range(1, len(s)):
            # add the next letter to the string
            if s[i] not in curr_letter_counts:
                curr_letter_counts[s[i]] = 0
            curr_letter_counts[s[i]] += 1
            
            max_curr_count_key = getMaxKey(curr_letter_counts)
            nc = numChanges(max_curr_count_key, curr_letter_counts)

            # check if it violates the condition
            if nc > k:
                #move up until removing s[substr_start_i] doesn't remove from the max letter
                while True:
                    # print(substr_start_i)
                    letter_to_remove = s[substr_start_i]
                    substr_start_i += 1
                    curr_letter_counts[letter_to_remove] -= 1

                    max_curr_count_key = getMaxKey(curr_letter_counts)
                    num_of_those_keys = getNumMaxKeys(max_curr_count_key, curr_letter_counts)
                    
                    if letter_to_remove != max_curr_count_key and num_of_those_keys == 1:
                        break
            
            # update the max_len
            curr_substr_len = i - (substr_start_i-1)
            max_len = max(max_len, curr_substr_len)
        return max_len


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
            
        