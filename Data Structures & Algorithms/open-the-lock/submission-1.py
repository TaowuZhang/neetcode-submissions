from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead = set(deadends)
        if '0000' in dead:
            return -1
        
        # 使用 BFS 队列：(当前状态, 当前步数)
        queue = deque([('0000', 0)])
        visited = {'0000'}
        
        while queue:
            curr, depth = queue.popleft()
            
            if curr == target:
                return depth
            
            # 生成 8 种可能的相邻状态
            for i in range(4):
                digit = int(curr[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    neighbor = curr[:i] + str(new_digit) + curr[i+1:]
                    
                    if neighbor not in visited and neighbor not in dead:
                        visited.add(neighbor)
                        queue.append((neighbor, depth + 1))
                        
        return -1