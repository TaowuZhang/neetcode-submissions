import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]  # (effort, r, c)
        
        while pq:
            effort, r, c = heapq.heappop(pq)
            
            if r == rows - 1 and c == cols - 1:
                return effort
            
            # 关键优化：如果当前弹出的 effort 已经大于已知最短路径，直接跳过
            if effort > dist[r][c]:
                continue
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))
        return 0