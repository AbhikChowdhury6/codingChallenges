from icecream import ic


def is_pal(s):
    if len(s) == 1 or len(s) == 0:
        return True
    
    first_half = s[:len(s)//2]

    second_half_start_idx = len(s)//2
    second_half_start_idx += 1 if len(s) % 2 == 1 else 0
    second_half_reversed = s[second_half_start_idx:][::-1]
    
    #ic(first_half, second_half_reversed)
    if first_half == second_half_reversed:
        return True
    return False


def lps(s):
    #check every possible length starting from the top
    for candidate_length in range(len(s), 0, -1):
        #ic(candidate_length)
        for poss_starting_idx in range(len(s) - candidate_length + 1):
            #ic(poss_starting_idx)
            end_idx = poss_starting_idx + candidate_length
            string_to_test = s[poss_starting_idx:end_idx]
            is_it_pal = is_pal(string_to_test)
            #ic(is_it_pal, string_to_test, poss_starting_idx, end_idx, candidate_length)
            if(is_it_pal):
                return string_to_test


lps("babad")