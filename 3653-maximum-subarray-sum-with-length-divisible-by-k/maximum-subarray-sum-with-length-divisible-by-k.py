class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        pre = [float("inf")] * k
        pre[0] = 0
        res = float("-inf")
        total = 0

        for i, n in enumerate(nums):
            total += n
            length = i + 1
            pre_len = length % k
            res = max(res, total - pre[pre_len])

            pre[pre_len] = min(pre[pre_len], total)
        return res