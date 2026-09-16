class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] += (dp[i-1][j] if i > 0 else 0) + (dp[i][j-1] if j > 0 else 0)
        return dp[n-1][m-1]
