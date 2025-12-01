class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries) // n


        while left < right:
            mid = right - (right - left) // 2

            extra = 0   
            for mn in batteries:
                extra += min (mn, mid)
            
            if extra // n >= mid:
                left = mid
            else:
                right = mid - 1
        
        return left