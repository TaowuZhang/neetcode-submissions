class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        # 边界情况：当只有一个人时，无需任何信任，他就是法官
        if n == 1 and not trust:
            return 1
            
        # 记录每个人的入度和出度
        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)
        
        for a, b in trust:
            out_degree[a] += 1
            in_degree[b] += 1
            
        # 检查是否有人满足条件：入度为 n-1 且出度为 0
        for i in range(1, n + 1):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i
                
        return -1