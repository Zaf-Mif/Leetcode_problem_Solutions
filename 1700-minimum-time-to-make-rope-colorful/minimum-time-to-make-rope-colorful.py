class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cnt = 0
        grp = ["".join(g) for i , g in groupby(colors)]
        # print(grp)
        k = 0
        for i in range(len(grp)):
            print(neededTime[k: k + len(grp[i])])
            cnt += (max(neededTime[k: k + len(grp[i])]))
            # print(cnt)
            k += len(grp[i])
        return (sum(neededTime) - cnt)