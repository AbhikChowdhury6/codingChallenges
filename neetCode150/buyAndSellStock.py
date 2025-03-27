class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # new plan
        # two pointers at the beginning
        # the first one is for the lowest low so far
        # the next one is for the highest high so far

        #there is only the opportunity to make more money if 
        # the right pointer finds a lower low
        # if it does, update our low pointer
        # keep a running max since the lowest low might not be followed by the max profit
        low_i = 0
        max_profit = 0
        for curr_i in range(1, len(prices)):
            if prices[curr_i] - prices[low_i] > max_profit:
                max_profit = prices[curr_i] - prices[low_i] 
            
            if prices[curr_i] < prices[low_i]:
                low_i = curr_i 
        return max_profit

