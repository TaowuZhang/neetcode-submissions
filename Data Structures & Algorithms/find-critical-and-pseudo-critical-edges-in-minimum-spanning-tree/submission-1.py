from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            # 路径压缩
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i, root_j = self.find(i), self.find(j)
        if root_i == root_j:
            return False
        # 按秩合并
        if self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        elif self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
        self.count -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 1. 记下原始索引，因为排序后索引会乱
        for i, edge in enumerate(edges):
            edge.append(i)
            
        # 2. 按边权从小到大排序
        edges.sort(key=lambda x: x[2])
        
        # 跑 Kruskal 算法的核心函数
        def get_mst_weight(exclude_idx: int = -1, include_idx: int = -1) -> float:
            uf = UnionFind(n)
            weight = 0
            
            # 如果强制包含某条边，起手先把它连上
            if include_idx != -1:
                u, v, w, _ = edges[include_idx]
                uf.union(u, v)
                weight += w
                
            # 按权重顺序贪心连边
            for i, (u, v, w, _) in enumerate(edges):
                if i == exclude_idx:
                    continue
                if uf.union(u, v):
                    weight += w
                    
            # 判断是否成功连成了一棵树（连通分量是否为 1）
            return weight if uf.count == 1 else float('inf')

        # 3. 先摸一次底，拿到标准 MST 的最小总权重
        base_weight = get_mst_weight()
        critical, pseudo = [], []
        
        # 4. 枚举每一条边，判断身份
        for i in range(len(edges)):
            orig_idx = edges[i][3]
            
            # 判断关键边：如果删掉它，连不通或者权重变大了
            if get_mst_weight(exclude_idx=i) > base_weight:
                critical.append(orig_idx)
            # 判断伪关键边：既然不是关键边，那如果强行提前选它，权重还是没变，说明它能上某辆末班车
            elif get_mst_weight(include_idx=i) == base_weight:
                pseudo.append(orig_idx)
                
        return [critical, pseudo]