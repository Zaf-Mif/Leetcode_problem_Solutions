class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums :
            return 0
            
        num = set(nums)
    
        mx = 1

        for x in num:
            if x - 1 not in num:
                curr = x
                cnt = 1

                while curr + 1 in num:
                    curr += 1
                    cnt += 1

                mx = max(mx, cnt)
        return mx