class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        setn = set(nums)
        flag = True
        while flag:
            if original in setn:
                original *= 2
            else:
                flag = False
        return original