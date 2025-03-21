from bisect import bisect_left, bisect_right
from icecream import ic

def findMedianSortedArrays(nums1, nums2) -> float:
    total_len = len(nums1) + len(nums2)
    is_total_len_even = total_len % 2 == 0 
    medianidx = total_len // 2

    def get_score_range(l1,l2, candidate):
        ic(l1, candidate)
        if len(l1) > 0:
            bl_l1 = bisect_left(l1, candidate)
            br_l1 = bisect_right(l1, candidate)
            if ((br_l1 > 0 and br_l1 < len(l1)) or l1[-1] == candidate) and candidate in l1 and candidate not in l2:
                br_l1 -=1
        else:
            bl_l1 = 0
            br_l1 = 0

        if len(l2) > 0:
            bl_l2 = bisect_left(l2, candidate)
            br_l2 = bisect_right(l2, candidate)
            if ((br_l2 > 0 and br_l2 < len(l2)) or l2[-1] == candidate) and candidate in l2 and candidate not in l1:
                br_l2 -=1
        else:
            bl_l2 = 0
            br_l2 = 0
        
        scoreMin = bl_l1 + bl_l2
        scoreMax = br_l1 + br_l2
        ic(bl_l1, bl_l2, br_l1, br_l2)
        return (scoreMin, scoreMax)

    def check_if_candidate_hits_score(scoreMin, scoreMax, targetIdx):
        return targetIdx >= scoreMin and targetIdx <= scoreMax
    
    def get_idx_median(nums1, nums2, targetIdx):
        ic(targetIdx)
        #first search nums 1
        curr_median_guess_idx = len(nums1)//2
        last_guess = -1
        go_to_nums2 = False
        while curr_median_guess_idx >= 0 and curr_median_guess_idx < len(nums1) and len(nums1) > 0:
            ic(curr_median_guess_idx)
            candidate_median = nums1[curr_median_guess_idx]
            scoreMin, scoreMax = get_score_range(nums1, nums2, candidate_median)
            ic(candidate_median, scoreMin, scoreMax)
            
            if check_if_candidate_hits_score(scoreMin, scoreMax, targetIdx):
                print("in retrun 1")
                return candidate_median
            last_last_guess = last_guess
            last_guess = curr_median_guess_idx
            if scoreMax < targetIdx:
                curr_median_guess_idx += ((len(nums1) - (curr_median_guess_idx + 1)) //2) +1

            if scoreMin > targetIdx:
                curr_median_guess_idx -= (curr_median_guess_idx - 1 //2) + 1
            
            if curr_median_guess_idx == last_last_guess:
                break
        
        curr_median_guess_idx = len(nums2)//2
        while curr_median_guess_idx >= 0 and curr_median_guess_idx < len(nums2):
            ic(curr_median_guess_idx)
            candidate_median = nums2[curr_median_guess_idx]
            scoreMin, scoreMax = get_score_range(nums1, nums2, candidate_median)
            ic(candidate_median, scoreMin, scoreMax)
            
            if check_if_candidate_hits_score(scoreMin, scoreMax, targetIdx):
                print("in retrun 2")
                return candidate_median
            
            if scoreMax < targetIdx:
                curr_median_guess_idx += ((len(nums2) - (curr_median_guess_idx + 1)) //2) +1

            if scoreMin > targetIdx:
                curr_median_guess_idx -= (curr_median_guess_idx - 1 //2) + 1
        return 0

    
    if not is_total_len_even:
        return get_idx_median(nums1, nums2, medianidx)
    
    return (get_idx_median(nums1, nums2, medianidx) + get_idx_median(nums1, nums2, medianidx - 1)) /2


l1 = []
l2 = [1,2,3,4]
print(findMedianSortedArrays(l1,l2))






# #for some reason this worked even though it is not the right complexity
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         a1idx = 0
#         a2idx = 0
#         total_len = len(nums1) + len(nums2)
#         medianidx = total_len // 2
#         # if total_len is even avg it with the number at the index before it
#         #kinda a binary search going back and forth untill we have all the values we need
        
#         # we're looking for a median value of two sorted lists
        
        
#         merged_list = sorted(nums1 + nums2)
#         if total_len %2 == 0:
#             return (merged_list[medianidx] + merged_list[medianidx-1])/2
#         return merged_list[medianidx] 
        