class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        remain = n % 7
        total = 0
        for i in range(weeks):
            total += 7 * (i + 1) + 21  
        
        start_day = weeks + 1
        for i in range(remain):
            total += start_day + i
        
        return total