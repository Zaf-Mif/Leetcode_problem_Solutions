class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for c in nums:
            freq[c] += 1
        
        pairs = freq.items()
        pairs = sorted(pairs, key=lambda item: (item[1], -item[0]))
        res = []
        for key, value in pairs:
            for i in range(value):
                res.append(key)
        return res