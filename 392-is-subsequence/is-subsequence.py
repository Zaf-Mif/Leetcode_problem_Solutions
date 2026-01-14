class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Use two-pointer approach: O(m+n) time, O(1) space
        # instead of DP: O(m*n) time, O(m*n) space
        s_idx = 0
        
        for char in t:
            if s_idx < len(s) and s[s_idx] == char:
                s_idx += 1
        
        return s_idx == len(s)