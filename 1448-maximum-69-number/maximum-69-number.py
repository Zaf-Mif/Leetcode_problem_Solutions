class Solution:
    def maximum69Number (self, num: int) -> int:
        #  changing the first 6 to 9 make the num higher 
        idx = 0
        #  store the first occurence of 6 and change it to 9 
        nums = str(num)
        for i in range(len(nums)):
            if nums[i] == '6':
                idx = i
                break
        #  iterate and change the idx to 9 
        ans = ''
        for i in range(len(nums)):
            if i == idx and nums[idx] == "6": 
                ans += '9'
                continue
            ans += nums[i]
        # print(ans, idx , nums)
        return int(ans)
            



