from collections import defaultdict

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # 1. 构建图
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1.0 / val
        
        # 2. 定义 DFS 搜索
        def dfs(curr, target, visited):
            # 如果节点不在图中，直接返回 -1.0
            if curr not in graph or target not in graph:
                return -1.0
            # 找到目标
            if curr == target:
                return 1.0
            
            visited.add(curr)
            for neighbor, weight in graph[curr].items():
                if neighbor not in visited:
                    res = dfs(neighbor, target, visited)
                    if res != -1.0:
                        return weight * res
            return -1.0

        # 3. 处理查询
        results = []
        for start, end in queries:
            results.append(dfs(start, end, set()))
            
        return results