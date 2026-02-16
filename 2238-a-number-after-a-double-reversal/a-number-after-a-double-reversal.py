class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        last = num % 10
        if num == 0:
            return True 
        return False if last == 0 else True
 