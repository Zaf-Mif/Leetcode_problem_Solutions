class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []

        for i in range(len(nums)-k+1):
            cnt = Counter(nums[i:i+k])
            if len(cnt) <= x:
                res.append(sum(nums[i:i+k]))
            else:
                pairs = list(cnt.items())
                pairs.sort(key=lambda p: (p[1], p[0]), reverse=True)
                cur = 0
                for num , value in pairs[:x]:
                    cur += (num*value)
                res.append(cur)
        return res


