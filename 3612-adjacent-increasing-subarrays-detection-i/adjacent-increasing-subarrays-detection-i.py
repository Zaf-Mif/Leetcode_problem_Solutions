class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n =len(nums)
        cnt, percent, ans = 1, 0, 0
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                cnt += 1
            else:
                percent, cnt = cnt, 1
            ans = max(ans, min(percent,cnt))
            ans = max(ans, cnt // 2)
        return ans >= k