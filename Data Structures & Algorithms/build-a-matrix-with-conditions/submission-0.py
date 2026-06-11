from collections import deque, defaultdict
from typing import List

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        # 🟣 漂亮结构：抽离出的标准拓扑排序模块
        def topo_sort(conditions):
            adj = defaultdict(list)
            indegree = {i: 0 for i in range(1, k + 1)}
            
            # 建有向图与入度表
            for u, v in conditions:
                adj[u].append(v)
                indegree[v] += 1
                
            # 找到所有入度为 0 的起点压入队列
            q = deque([i for i in range(1, k + 1) if indegree[i] == 0])
            order = []
            
            # BFS 剥洋葱
            while q:
                node = q.popleft()
                order.append(node)
                for neighbor in adj[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
                        
            # 🔴 如果存在环，剥不干净 k 个节点，直接返回空
            return order if len(order) == k else []

        # 1. 分别跑两次独立的拓扑排序
        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)
        
        # 2. 只要有一边撞上了悬崖（有环无解），则整体无解
        if not row_order or not col_order:
            return []
            
        # 3. 建立 [数字 -> 最终坐标] 的索引字典
        row_idx = {num: i for i, num in enumerate(row_order)}
        col_idx = {num: i for i, num in enumerate(col_order)}
        
        # 4. 生成 k x k 的底盘并填入数值
        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[row_idx[num]][col_idx[num]] = num
            
        return matrix