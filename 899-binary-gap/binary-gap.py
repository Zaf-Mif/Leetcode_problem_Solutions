class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        if n == 1:
            return 0
        cont = 0 
        mx = 0
        for i in range(len(s)):
            if s[i] == "1":
                mx = max(mx, cont)
                cont = 1
            else:
                cont += 1
        if s[-1] == "1":
            mx = max(cont, mx)
        return mx 