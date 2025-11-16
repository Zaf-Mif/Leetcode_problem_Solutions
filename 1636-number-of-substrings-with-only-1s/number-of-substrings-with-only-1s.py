class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        flag = True
        temp = 0
        s1 = s.count('1')
        # print(s1)
        for i in range(len(s)):
            # print(res)
            if s[i] == '0':
                res += temp * (temp + 1) // 2 
                temp = 0
                flag = True
            else:
                if flag:
                    temp += 1
        res += temp * (temp + 1) // 2 
        res %= 10**9 + 7
        return res
