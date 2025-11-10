class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        #  if the next array is greater than >= 
        cnt = 0
        if len(timeSeries)==0:
            return 0
        for i in range(len(timeSeries)-1):
            cnt += min(timeSeries[i+1]- timeSeries[i] , duration)
            
        return cnt + duration
