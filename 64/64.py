class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp 
        row = len(grid)       
        col = len(grid[0])
        dp = [[0 for i in range(col)] for i in range(row)]
        for i in range(0,row):
            for j in range(0,col):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j > 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0 and i > 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]