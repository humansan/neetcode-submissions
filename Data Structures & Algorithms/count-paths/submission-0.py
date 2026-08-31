class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp_grid = [[0] * n for _ in range(m)]
        dp_grid[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp_grid[i][j] += dp_grid[i-1][j]
                
                if j > 0:
                    dp_grid[i][j] += dp_grid[i][j-1]
        
        return dp_grid[m-1][n-1]
