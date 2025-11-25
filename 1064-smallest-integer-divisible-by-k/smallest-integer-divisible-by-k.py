class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        rem = 0
        l = 0
        while True:
            rem = (rem * 10 +1) % k
            l += 1
            if rem == 0:
                return l
