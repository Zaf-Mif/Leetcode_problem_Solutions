class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for ch in operations:
            if ch == "++X" or ch == "X++":
                x += 1
            else:
                x -= 1
        return x