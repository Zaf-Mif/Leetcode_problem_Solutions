class Solution:
    def makeFancyString(self, s: str) -> str:
        ss = ''
        # for i in range(1,len(s)-1):
        #     if s[i-1] == s[i] and s[i]== s[i-1]:
        #         ss += s[i] * 2
        #     if (s[i-1] != s[i] and s[i] == s[i+1] or
        #         s[i-1] == s[i] and s[i] != s[i+1] or 
        #         s[i-1] != s[i] and s[i] != s[i+1]) : 
        #         if i-1 == 0 :
        #             ss += s[i-1]
        #         ss += s[i]
        # return ss
        prev = s[0]
        frequency = 1
        ans = s[0]

        for i in range(1, len(s)):
            if s[i] == prev:
                frequency += 1
            else:
                prev = s[i]
                frequency = 1

            if frequency < 3:
                ans += s[i]

        return ans