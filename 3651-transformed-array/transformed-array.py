class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * N
        for i, x in enumerate(nums):
            res[i] = nums[(i + x) % N]
        return res