class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n == 1:
            return 0
        
        nums.sort()
        rs = n
        right = 0
        for left in range(n):
            while right < n and nums[right] <= nums[left] * k:
                right += 1
            rs = min(rs, n - (right - left))

        return rs