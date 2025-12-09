class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for v in nums:
            ans.append(v)
        for v in nums:
            ans.append(v)
        return ans