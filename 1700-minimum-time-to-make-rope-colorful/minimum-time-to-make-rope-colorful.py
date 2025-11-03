class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        l = 0
        cnt = 0
        for r in range(n):
            if colors[r] != colors[l]:
                same = neededTime[l:r]
                cnt += sum(same) - max(same)
                l = r
        cnt += sum(neededTime[l:]) - max(neededTime[l:])
        return cnt 