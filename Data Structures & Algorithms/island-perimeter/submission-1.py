class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # 假设每一格贡献 4 条边
                    perimeter += 4
                    
                    # 如果上方有土地，减去两个共享边
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    # 如果左方有土地，减去两个共享边
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
                        
        return perimeter