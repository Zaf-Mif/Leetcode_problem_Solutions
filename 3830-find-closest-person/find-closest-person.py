class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        p1 = x-z if x > z else z-x
        p2 = y-z if y > z else z-y

        if p1 < p2:
            return 1
        elif p1 > p2:
            return 2
        elif p1 == p2:
            return 0
