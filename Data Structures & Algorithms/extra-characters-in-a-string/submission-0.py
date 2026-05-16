class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        word_set = set(dictionary)
        n = len(s)
        # dp[i] 表示 s[0:i] 的最少多余字符
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # 默认情况：当前字符 s[i-1] 是多余的
            dp[i] = dp[i - 1] + 1
            
            # 尝试看有没有以 s[i-1] 结尾的单词
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])
                    
        return dp[n]