import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # 将 project 组合起来并按需要的启动资金 capital 从小到大排序
        projects = sorted(zip(capital, profits))
        
        max_heap = []
        i = 0
        n = len(projects)
        
        # 最多进行 k 次项目选择
        for _ in range(k):
            # 将所有当前资本 w 能够负担的项目，将其利润放入最大堆中
            # Python 默认是最小堆，所以存入负值来模拟最大堆
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            
            # 如果最大堆为空，说明当前资本无法启动任何新项目
            if not max_heap:
                break
                
            # 贪心选择：挑选利润最大的项目
            w += -heapq.heappop(max_heap)
            
        return w