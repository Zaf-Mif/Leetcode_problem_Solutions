class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d=(x-y)*(x+y-2*z)
        if d < 0:  return 1
        elif d > 0: return 2
        else: return 0