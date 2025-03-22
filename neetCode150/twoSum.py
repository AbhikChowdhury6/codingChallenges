class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            compliment = target - nums[i]
            sub_list = nums[:i] + nums[i+1:]
            if compliment not in sub_list:
                continue
            comp_idx = sub_list.index(compliment)
            comp_idx += 1 if comp_idx >= i else 0
            return [i, comp_idx]