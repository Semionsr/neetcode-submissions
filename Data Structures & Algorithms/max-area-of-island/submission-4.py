class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        checker = set()
        ROWS,COLS = len(grid), len(grid[0])
        area = 0

        
        def dfs(r,c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r,c) in checker or grid[r][c] != 1):
                return 0
            area = 1
            checker.add((r,c))
            
            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r,c+1)
            area += dfs(r,c-1)
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == 1 and (r,c) not in checker):
                    area = max(area, dfs(r,c))
        return area
                