class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        if 1 in nums: return False
        
        # 最大数值限制
        MAX_VAL = 100000
        # 并查集容量：n 个数字下标 + MAX_VAL 个质数节点
        uf = UnionFind(n + MAX_VAL + 1)
        
        for i, val in enumerate(nums):
            d = 2
            temp = val
            while d * d <= temp:
                if temp % d == 0:
                    # 将下标 i 与质因子 d 绑定
                    uf.union(i, n + d)
                    while temp % d == 0:
                        temp //= d
                d += 1
            if temp > 1:
                # 剩余的质因子
                uf.union(i, n + temp)
        
        # 检查所有下标是否连通到同一个根节点
        root = uf.find(0)
        for i in range(1, n):
            if uf.find(i) != root:
                return False
        return True

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, i):
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j