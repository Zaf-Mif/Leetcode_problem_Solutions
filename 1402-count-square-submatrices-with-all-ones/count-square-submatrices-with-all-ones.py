class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        Rows, Cols = len(matrix), len(matrix[0])
        dp = [[0] * (Cols + 1) for _ in range(Rows + 1)]
        ans = 0
        for row in range(Rows):
            for col in range(Cols):
                if matrix[row][col]:
                    dp[row + 1][col + 1] = (
                        min(dp[row][col + 1], dp[row + 1][col], dp[row][col]) + 1
                    )
                    ans += dp[row + 1][col + 1]
        return ans