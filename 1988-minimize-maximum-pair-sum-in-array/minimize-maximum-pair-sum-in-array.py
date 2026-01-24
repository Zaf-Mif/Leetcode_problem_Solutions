class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        mx = 0
        for i in range(len(nums)// 2):
            mx = max(mx, nums[i] + nums[len(nums) - 1 - i])
        return mx