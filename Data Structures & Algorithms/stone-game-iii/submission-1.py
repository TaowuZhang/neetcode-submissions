class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        # dp[i] 表示从i开始的相对最大分差
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            res = float('-inf')
            current_sum = 0
            # 尝试取 1, 2, 或 3 个石子
            for k in range(1, 4):
                if i + k <= n:
                    current_sum += stoneValue[i + k - 1]
                    res = max(res, current_sum - dp[i + k])
            dp[i] = res
            
        if dp[0] > 0: return "Alice"
        if dp[0] < 0: return "Bob"
        return "Tie"