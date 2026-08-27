class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        distance = 0
        visit = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        def addcell(r,c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                grid[r][c] == -1 or (r,c) in visit or grid[r][c] == 0):
                return
            visit.add((r,c))
            grid[r][c] = distance
            q.append((r,c))


        while q:
            qlen = len(q)
            distance += 1
            
            for i in range(qlen):
                r, c = q.popleft()
                for dr,dc in directions:
                    addcell(r+dr,c+dc)
            
            #distance += 1

