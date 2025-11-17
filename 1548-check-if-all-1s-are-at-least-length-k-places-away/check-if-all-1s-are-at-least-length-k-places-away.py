class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        continuos = k

        for n in nums:
            if n == 1:
                if continuos < k:
                    return False
                continuos = 0
            else:
                continuos += 1

        return True