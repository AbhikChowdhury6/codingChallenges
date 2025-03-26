class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        derivitives =  [prices[i+1] - prices[i] for i in range(len(prices)-1)]
        return max([])
        curr_valley_idx = 0
        curr_peak_idx = len(prices) - 1
        max_return = 0
        while curr_valley_idx < curr_peak_idx:
            #calc next valley idx

            #calc prev peak idx
            
            #if the condition is met
            # move either or both 
            pass
