class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        cnp = operations.count("++X") + operations.count("X++")
        cnm = operations.count("--X") + operations.count("X--")
        x += cnp
        x -= cnm
        return x