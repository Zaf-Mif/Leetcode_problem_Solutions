class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        mx = 0
        for i in nums:
            if i == 1:
                cnt += 1
                mx = max(mx, cnt)
            else:
                cnt = 0
        return mx
