class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            rem = num % 3
            res += min(3-rem, rem)
        return res
