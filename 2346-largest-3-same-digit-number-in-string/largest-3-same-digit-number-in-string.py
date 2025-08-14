class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        s = "" 
        for i in range(1, len(nums) - 1):
            if nums[i - 1] == nums[i] == nums[i + 1]:
                triplet = nums[i - 1:i + 2]
                if s == "" or triplet > s:
                    s = triplet
        return s
