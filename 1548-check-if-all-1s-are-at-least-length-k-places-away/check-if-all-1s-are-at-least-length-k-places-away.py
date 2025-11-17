class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        idx = 0
        first = True
        for i in range(len(nums)):
            print(idx)
            if first == True and nums[i] == 1:
                first = False
                idx = i
            elif nums[i] == 1 and first == False:
                if (i - idx) - 1 < k :
                    return False
                idx = i
        return True
