class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0 : # k==5
            return -1
        cnt = 1
        ans = 1
        while cnt % k != 0:
            cnt = cnt * 10 + 1
            ans+= 1

        return ans

                
        
                



            

        