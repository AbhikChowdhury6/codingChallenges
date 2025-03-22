class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        all_letters = set(s).union(set(t))
        return all([list(s).count(x) == list(t).count(x) for x in all_letters])
        