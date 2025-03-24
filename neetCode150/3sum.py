#forgot to tuplize on existing sums2
#empty double curly braces doesn't initialize a set
#i was adding an unhashable type to a set
#it's treating the orders as different which it shouldn't apparently
#i thought sorted tuple, but only did sorted
#when I intiially thought through the algo I knew i had to check that the searching index
# shouldn't be duplicated but i forgot to include it

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # calc double sums in a dict
        tups = [(x,y) for x in range(len(nums)) for y in range(len(nums)) if x != y]
        print(tups)
        sums2 = {}
        for x,y in tups:
            val = nums[x] + nums[y]
            if val not in sums2:
                sums2[val] = [(x,y)]
            else:
                sums2[val].append((x,y))

        # for each element generate all lists with the complement in the dict
        set_to_return = set()
        for i, num in enumerate(nums):
            if -num not in sums2:
                continue
            
            for x,y in sums2[-num]:
                if x ==i or y == i:
                    continue
                set_to_return.add(tuple(sorted([num, nums[x], nums[y]])))
        
        return [[x,y,z] for x,y,z in set_to_return]
        