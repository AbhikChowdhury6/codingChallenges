from bisect import bisect_left
from icecream import ic

def twoSum(numbers, target: int):
    #find where the compliment would be and check if it's there
    for i in range(len(numbers)):
        potential_compliment = target - numbers[i]
        potential_loc = bisect_left(numbers[i:], potential_compliment) + i
        #ic(potential_compliment, potential_loc)
        if potential_loc == len(numbers):
            continue
        #ic(numbers[potential_loc])
        if numbers[potential_loc] == potential_compliment:
            return [i+1, potential_loc+1]


#forgot to add the +1 index from the description
#didn't check for compliments that would be larger than all other elements in the list and at index len
# is searched the shortend list but forgot to add back in the i offset

numbers=[-5,-3,0,2,4,6,8]
target=5
print(twoSum(numbers, target))