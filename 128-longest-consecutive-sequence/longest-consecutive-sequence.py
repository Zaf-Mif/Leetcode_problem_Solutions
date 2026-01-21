class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # without following o(n)
        if len(nums) == 0 :
            return 0
        num = list(set(nums))
        if len(num) == 1:
            return 1

        num.sort()
        temp = 1
        mx = 1

        print(num)
        for i in range(len(num)-1):
            # if temp == 0 and num[i] + 1 == num[i+1]:
            #     temp += 2
            if num[i] + 1 == num[i+1]:
                temp += 1
            else:
                mx = max(mx, temp)
                temp = 1
        mx = max(mx, temp)
        return mx 