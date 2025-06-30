class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        freq = Counter(nums)
        if len(freq) == 1:
            return 0

        mx = 0
        for key, val in freq.items():
            if key-1 in freq:
                mx = max(mx, val + freq[key-1])
        return mx
