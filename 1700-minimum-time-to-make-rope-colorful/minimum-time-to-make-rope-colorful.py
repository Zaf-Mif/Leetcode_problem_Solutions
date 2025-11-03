class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cnt = 0
        grp, temp = [], colors[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                temp += (colors[i])
            else:
                grp.append(temp)
                temp = colors[i]
        grp.append(temp)
        # print(grp)
        k = 0
        for i in range(len(grp)):
            # print(neededTime[k: k + len(grp[i])])
            cnt += (max(neededTime[k: k + len(grp[i])]))
            # print(cnt)
            k += len(grp[i])
        return sum(neededTime) - cnt