class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        mn = float('inf')
        arr.sort(reverse = True)
        for i in range(len(arr)-1):
            mn = min(mn, abs(arr[i]- arr[i+1]))
        # print(mn)
        res = []
        for i in range(len(arr)-1):
            if abs(arr[i] - arr[i+1]) == mn:
                res.append([arr[i+1], arr[i]])
        res.reverse()
        return res