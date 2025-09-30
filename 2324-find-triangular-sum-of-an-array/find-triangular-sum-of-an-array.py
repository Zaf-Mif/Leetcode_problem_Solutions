class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            num = list()
            for i in range(len(nums) - 1):
                num.append((nums[i] + nums[i + 1]) % 10)
            nums = num
        return nums[0]