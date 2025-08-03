class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        prefix = [0] * (n+1)
        idx = [0] * n 

        # prefix sum and idx 
        for i in range(n):
            prefix[i+1] = prefix[i] + fruits[i][1]
            idx[i] = fruits[i][0]

        ans = 0
        # left then right right then left only right only left 
        for x in range(k // 2 + 1):
            # left then right 
            # x step left then k-2x step right 
            y = k - 2 * x
            left = startPos - x
            right = startPos + y
            start = bisect_left(idx, left)
            end = bisect_right(idx, right)
            ans = max(ans, prefix[end] - prefix[start])


            # right then left 
            # x step right then k-2x step left 
            y = k - 2 * x
            left = startPos - y
            right = startPos + x
            start = bisect_left(idx, left)
            end = bisect_right(idx, right)
            ans = max(ans, prefix[end] - prefix[start])
        
        return ans



