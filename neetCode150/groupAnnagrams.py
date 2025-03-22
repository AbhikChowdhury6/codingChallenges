class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set_list = []
        output_list = []
        for s in strs:
            s_set = set([(x, s.count(x)) for x in set(s)])
            if s_set not in set_list:
                set_list.append(s_set)
                output_list.append([s])
            else:
                output_list[set_list.index(s_set)].append(s)
        return output_list