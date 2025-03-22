class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #frequencies = sorted(list(set([(x, nums.count(x)) for x in nums])), key=lambda x:-x[1])
        #return [x[0] for x in frequencies[:k]]
        freqs = {}
        for n in nums:
            if n not in freqs:
                freqs[n] = 0
            freqs[n] += 1
        freq_tuples = [(x, freqs[x]) for x in freqs]
        sorted_freqs = sorted(freq_tuples, key = lambda x: -x[1]) #reversd order based on frequencies
        return [x[0] for x in sorted_freqs[:k]]
        