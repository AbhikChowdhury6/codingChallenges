from icecream import ic

# gawd dammit, i actually had to use the hints.
# i'll sleep on the moving the pointers in condition and figure it out

# alright so this optimization probelm is convex
# we first looked at the the function we were optimizing
# then we initialized at he maximum value of of one of the two terms (width)
# then we moved one of the indexes that had the opportunity to increase the height
# it's the less one for sure becuse of the min function
# if they are even, either way the width is being reduced by 1
# and the max possible height of the next iteration will be the same


def maxArea(heights) -> int:
    #start at the ends and move in if gainz are on the table
    start_idx = 0
    end_idx = len(heights) - 1
    curr_max_vol = min(heights[start_idx], heights[end_idx]) * (end_idx - start_idx)
    while start_idx < end_idx:
        next_width = end_idx - start_idx
        this_vol = min(heights[start_idx], heights[end_idx]) * next_width
        curr_max_vol = max([curr_max_vol, this_vol])
        print(start_idx)
        print(end_idx)
        #keep going untill i gain more bringing in an index
        # moving the end left looses more than  i gain in index
        # when checking to jump check both sides
        # and move the smaller one
        
        if heights[start_idx] <= heights[end_idx]:
            start_idx += 1
        else:
            end_idx -= 1
    return curr_max_vol
    

height=[1,7,2,5,12,3,500,500,7,8,4,7,3,6]
print(maxArea(height))