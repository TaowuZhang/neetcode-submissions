"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        return self.build(grid, 0, 0, len(grid))
    
    def build(self, grid, r, c, n):
        # 检查当前区域是否所有值都相同
        if self.allSame(grid, r, c, n):
            # val 为 True (1) 或 False (0)
            return Node(grid[r][c] == 1, True)
        
        # 如果不相同，递归分裂
        half = n // 2
        root = Node(True, False) # 内部节点的 val 可以为任意值
        
        root.topLeft = self.build(grid, r, c, half)
        root.topRight = self.build(grid, r, c + half, half)
        root.bottomLeft = self.build(grid, r + half, c, half)
        root.bottomRight = self.build(grid, r + half, c + half, half)
        
        return root

    def allSame(self, grid, r, c, n):
        val = grid[r][c]
        for i in range(r, r + n):
            for j in range(c, c + n):
                if grid[i][j] != val:
                    return False
        return True