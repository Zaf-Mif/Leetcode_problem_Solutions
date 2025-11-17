class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        continuos = k

        for i in range(len(nums)):
            if nums[i] == 0:
                continuos += 1
            else:
                
                if continuos < k:
                    return False
                continuos = 0
        return True