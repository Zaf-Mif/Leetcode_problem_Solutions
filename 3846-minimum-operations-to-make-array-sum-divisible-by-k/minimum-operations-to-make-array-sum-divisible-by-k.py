class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        mn = float("-inf")
        sm = sum(nums)
        if sm % k == 0:
            return 0
        
        rem = sm % k 
        return rem