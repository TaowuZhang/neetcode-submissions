from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1: 
            return [0]
        
        # 1. 初始化度表和邻接表
        adj = [set() for _ in range(n)]
        degree = [0] * n
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            degree[u] += 1
            degree[v] += 1
            
        # 2. 找到所有初始叶子
        leaves = deque([i for i in range(n) if degree[i] == 1])
        
        # 3. 剥离直到只剩 1 或 2 个节点
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                # 找到叶子的邻居并移除连接
                # 注意：pop() 操作会改变集合，是安全的
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                degree[neighbor] -= 1
                
                if degree[neighbor] == 1:
                    leaves.append(neighbor)
                    
        return list(leaves)