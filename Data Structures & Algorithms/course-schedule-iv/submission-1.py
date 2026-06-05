class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        # 初始化邻接矩阵
        is_prereq = [[False] * numCourses for _ in range(numCourses)]
        
        # 填入直接依赖
        for u, v in prerequisites:
            is_prereq[u][v] = True
            
        # Floyd-Warshall 传递闭包
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    # 如果 i 到 k 有路径，且 k 到 j 有路径，则 i 到 j 有路径
                    if is_prereq[i][k] and is_prereq[k][j]:
                        is_prereq[i][j] = True
                        
        # 处理查询
        return [is_prereq[u][v] for u, v in queries]