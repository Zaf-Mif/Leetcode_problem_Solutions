class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res += min(3-num % 3, num % 3)
        return res
