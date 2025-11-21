class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        let = set(s)
        ans = 0
        
        for l in let:
            i, j = s.index(l), s.rindex(l)
            between = set()
            
            for k in range(i + 1, j):
                between.add(s[k])
            
            ans += len(between)

        return ans