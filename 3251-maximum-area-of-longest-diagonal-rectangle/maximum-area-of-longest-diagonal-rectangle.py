class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        mx = 0
        ans = 0
        for l, w in dimensions:
            h = sqrt(l**2 + w**2)
            res = l * w
            if mx < h:
                mx = h
                ans = res
            elif h == mx:
                ans = max(res, ans)
        return ans