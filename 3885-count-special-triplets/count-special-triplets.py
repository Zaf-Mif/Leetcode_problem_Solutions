class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        num = {}
        freq = {}

        for v in nums:
            num[v] = num.get(v, 0) + 1

        ans = 0
        for v in nums:
            target = v * 2
            lcnt = freq.get(target, 0)
            freq[v] = freq.get(v, 0) + 1
            rcnt = num.get(target, 0) - freq.get(target, 0)
            ans = (ans + lcnt * rcnt) % MOD

        return ans