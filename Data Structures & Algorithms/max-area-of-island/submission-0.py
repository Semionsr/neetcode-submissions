class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        area = 0
        

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            cur = 1


            while q:
                r,c = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    if ((r+dr) in range(ROWS) and
                        (c+dc) in range(COLS) and
                        ((r+dr,c+dc) not in visit) and
                        (grid[r+dr][c+dc] == 1)):
                        cur += 1
                        q.append((r+dr, c+dc))
                        visit.add((r+dr, c+dc))
            return cur

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area,bfs(r,c))
                
        return area
