class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisors(n):
            cnt = set()
            d = 1
            while d * d <= n:
                if n % d == 0:
                    cnt.add(d)
                    cnt.add(n // d)
                    if len(cnt) > 4:
                        return 0
                d += 1
            return sum(cnt) if len(cnt) == 4 else 0
        sm = 0 
        for n in nums:
            sm += divisors(n)
        return sm
