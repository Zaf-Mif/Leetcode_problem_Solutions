class Solution:
    def maxSumNode(self, index, isEven, nums, k, memorization):
        if index == len(nums):
            return 0 if isEven == 1 else -float("inf")
        if memorization[index][isEven] != -1:
            return memorization[index][isEven]

        no = nums[index] + self.maxSumNode(index + 1, isEven, nums, k, memorization)
        xor = (nums[index] ^ k) + self.maxSumNode(
            index + 1, isEven ^ 1, nums, k, memorization
        )

        memorization[index][isEven] = max(xor, no)
        return memorization[index][isEven]

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        memorization = [[-1] * 2 for _ in range(len(nums))]
        return self.maxSumNode(0, 1, nums, k, memorization)