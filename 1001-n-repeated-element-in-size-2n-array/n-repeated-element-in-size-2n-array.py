class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # our n ln(nums)
        n = len(nums) // 2
        #  uniques == n + 1 and 
        #  [1,2,3,3] n = 4 // 2 = 2 and 3 unique elements 
        freq = defaultdict(int)
        for c in nums:
            freq[c] += 1
        return next(key for key, value in freq.items() if value == n)
        