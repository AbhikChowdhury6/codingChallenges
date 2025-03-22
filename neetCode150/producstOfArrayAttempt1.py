class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)

        # calc total excluding any zeroes
        total = 1
        for x in nums: total *= x if x != 0 else 1
        
        # no zeroes
        if nums.count(0) == 0:
            return [total//x for x in nums]

        # one zero
        list_to_return = [0] * len(nums)
        list_to_return[nums.index(0)] = total
        return list_to_return