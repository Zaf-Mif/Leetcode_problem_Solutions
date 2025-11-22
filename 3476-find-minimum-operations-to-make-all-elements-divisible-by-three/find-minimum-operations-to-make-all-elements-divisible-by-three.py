class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(min(3-num % 3, num % 3) for num in nums)
