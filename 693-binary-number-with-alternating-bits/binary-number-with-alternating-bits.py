class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n, last = divmod(n, 2)

        while n:
            if last == n % 2: 
                return False
            n, last = divmod(n, 2)

        return True