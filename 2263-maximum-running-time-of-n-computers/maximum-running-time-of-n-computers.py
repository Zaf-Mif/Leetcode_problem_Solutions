class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        extra = sum(batteries[:-n])
        live = batteries[-n:]

        for i in range(n-1):
            # when we try to distribute but it become less than there
            if extra // (i+1) < live[i+1] - live[i]:
                return live[i] + extra // (i+1)
            extra -= ((i+1) * (live[i+1] - live[i]))
            
        return extra // n + live[-1]