class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for c in nums:
            freq[c] += 1
        
        cnt = 0
        mx = max(freq.values())
        for key , value in freq.items():
            if value == mx:
                cnt += value
        
        return cnt
            
