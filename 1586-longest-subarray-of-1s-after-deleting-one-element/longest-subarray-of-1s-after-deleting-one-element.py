class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = curr = prev = 0
        for i in range(n):
            if nums[i] == 0:
                ans = max(ans, prev + curr)
                prev = curr
                curr = 0
            else:
                curr += 1
        
        if nums[-1] == 1:
            ans = max(ans , prev+ curr)
        
        if curr == n :
            return n-1
        
        return ans 
