class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # 使用一维数组记录当前行的路径数
        dp = [0] * n
        
        # 初始化：如果起点有障碍，则无法出发
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    # 当前路径数 = 来自上方(当前的dp[j]) + 来自左方(dp[j-1])
                    # 注意：如果是第一行，dp[j] 依然是 0（因为上方不可达），逻辑兼容
                    dp[j] += dp[j-1]
                    
        return dp[n-1]