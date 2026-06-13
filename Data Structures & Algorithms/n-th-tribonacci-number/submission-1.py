class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        
        # 初始化前三项
        a, b, c = 0, 1, 1
        
        # 迭代计算直到 n
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
            
        return c