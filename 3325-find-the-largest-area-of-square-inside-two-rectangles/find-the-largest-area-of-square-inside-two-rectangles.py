class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        mx = 0
        for (bfi, tri), (bli, trj,) in combinations(zip(bottomLeft, topRight), 2):
            w = min(tri[0], trj[0]) - max(bfi[0], bli[0])
            h = min(tri[1], trj[1]) - max(bfi[1], bli[1])

            mx = max(mx, min(w, h))

        return mx * mx