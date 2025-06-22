class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        ss = ""
        for word in s :
            ss += word
            if len(ss) == k:
                ans.append(ss)
                ss = ""
        if len(ss) > 0:
            ans.append(ss)
        if len(ans[-1]) != k: 
            remain = k - len(ans[-1])
            for i in range(remain):
                ans[-1] += fill
 
        return (ans)
        