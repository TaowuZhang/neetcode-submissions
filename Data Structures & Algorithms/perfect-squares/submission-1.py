class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] 表示和为 i 的完全平方数的最少数量
        dp = [i for i in range(n + 1)]
        
        # 从 1 到 n 进行动态规划
        for i in range(1, n + 1):
            j = 1
            # 遍历所有满足 j*j <= i 的完全平方数
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        return dp[n]