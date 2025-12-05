class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        pre = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            pre[i+1] = pre[i] + nums[i]
        # [0, 10, 20, 23, 30, 36]
        print(pre)
        # [0, 2, 6, 12, 20]
        cnt = 0
        for i in range(1, len(nums)):
            cnt += 1 if ((pre[i] % 2 == 0) == ((pre[-1] - pre[i]) % 2 == 0)) else 0
        return cnt 