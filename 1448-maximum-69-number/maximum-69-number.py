class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = str(num)
        ans = ''
        first = False
        for i in range(len(nums)):
            if not first and nums[i] == "6": 
                ans += '9'
                first = True
                continue
            ans += nums[i]
        # print(ans, idx , nums)
        return int(ans)
            



