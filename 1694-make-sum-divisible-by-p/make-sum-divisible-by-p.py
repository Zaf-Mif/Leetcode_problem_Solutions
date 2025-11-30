class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remain = total % p
        # print(total, remain)
        if remain == 0:
            return 0
        res = len(nums)
        cur = 0
        visit = {
            0: -1
        }
        for i, n in enumerate(nums):
            cur = (cur + n ) % p
            pre = (cur - remain + p) % p
            if pre in visit:
                length = i - visit[pre]
                res = min(res, length)
            
            visit[cur] = i
        return -1 if res == len(nums) else res