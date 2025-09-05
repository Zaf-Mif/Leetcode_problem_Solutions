class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(1,61):
            d = num1- num2 * i
            if d < i:
                return -1
            
            if i >= d.bit_count():
                return i
            
        return -1