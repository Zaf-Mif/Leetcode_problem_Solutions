class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        res = [] 
        freq = defaultdict(int)
        for c in nums:
            freq[c] += 1 
        pairs = sorted(freq.items(), key=lambda item: (item[1], -item[0]))
        for key, value in pairs:
            for i in range(value):
                res.append(key)
        return res