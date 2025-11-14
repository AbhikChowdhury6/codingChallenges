from bisect import bisect_left
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # woooo were so back
        # what were going to do
        # so one thing I liked was initializing the output array
        # and setting n to the len since well be using it a lot
        
        n = len(temperatures)
        res = [0] * n

        # so now were goint to iterate through the list forward
        # and while the numbers are monitonically decreasing well add them to the stack

        # and when we pop something off of the stack well calulate the difference between
        # that index and the index of the temp that caused it to get popped
        
        s = [[0, temperatures[0]]]
        for i in range(1, n):
            curr_temp = temperatures[i]
            while s and s[-1][1] < curr_temp:
                popping_idx, popping_val = s.pop()
                res[popping_idx] = i - popping_idx
            
            #add it to the stack
            s.append([i, temperatures[i]])
        
        return res



#A1
from types import List
from bisect import bisect_left
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # lets start with like a dynamic programming approach where 
        # I yes do a seach ahead, but keep an ordered dict of the numbers decending order
        # so when I get a new number I just see where it is in the dict and then calc the i difference

        # build dictionary
        # no actually that wouldnt work as well, since there could be many ups and downs
        # and we would have to also search for which one is to the right of it

        # that actually is still kinda easy, just have a sorted list of indexes as the values in the
        # ordered dict, also the int keys will hash to themselves so I dont even have to worry about that

        loc_dic = {}
        for i, t in enumerate(temperatures):
            if t not in loc_dic:
                loc_dic[t] = []
            loc_dic[t].append(i) #we're going from left to right so i is monotonically increasing
        
        temp_keys = loc_dic.keys()
        def next_highest_val(curr_temp):
            next_highest_index = bisect_left(temp_keys, curr_temp) + 1
            if next_highest_index == len(temp_keys) + 1:
                return None
            
            return temp_keys[next_highest_index]

        output_list = []
        for t in temperatures:
            higher_val = next_highest_val(t)
            if higher_val is None:
                output_list.append(0)
                continue
            

            # darn we dont just need the next highest val, we need if any of the higher vals
            # of course logically we could iterate over and append all of the lists for those higher
            # and then find the one closest but greater than i, but that deffo will make it n^2
            shit = loc_dic[higher_val]