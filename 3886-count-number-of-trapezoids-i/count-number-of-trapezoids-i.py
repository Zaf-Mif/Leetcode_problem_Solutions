class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # grouping points by thir y axis 
        # selecting 2 groups from the froups 
        MOD = 10 ** 9 + 7
        freq = defaultdict(int)
        for c in points:
            freq[c[1]] += 1
            # by using it's y-axis 
        res, total = 0, 0
        for val in freq.values():
            v = (val * (val-1)) // 2
            res = (res + v * total) % MOD
            total = (total + v) % MOD
        return res 
