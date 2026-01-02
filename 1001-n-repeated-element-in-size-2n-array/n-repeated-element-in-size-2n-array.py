class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # our n ln(nums)
        #  uniques == n + 1 and 
        #  [1,2,3,3] n = 4 // 2 = 2 and 3 unique elements 
        cnt = collections.Counter(nums)
        # print(cnt)
        for c in cnt:
            # print(c, cnt[c])
            if cnt[c] > 1:
                return c