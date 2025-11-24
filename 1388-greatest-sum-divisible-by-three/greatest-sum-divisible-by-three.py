class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        one =  float('inf')
        two = float('inf')
        total = 0
        for n in nums:
            total += n
            if n % 3 == 1:
                two = min(two, n + one)
                one = min(one, n)
            if n % 3 == 2:
                one = min(one , two +n)
                two = min(two, n)

        if total % 3 == 0:
            return total
        if total % 3 == 1:
            return total - one
        if total % 3 == 2:
            return total - two
        