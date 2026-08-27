class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = collections.deque()
        distance = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))


        def addcell(r,c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r,c) in visit or grid[r][c] == -1):
                return
            
            visit.add((r,c))
            q.append((r,c))
            

        while q:
            qlen = len(q)

            for i in range(qlen):
                r,c = q.popleft()
                grid[r][c] = distance
                addcell(r+1,c)
                addcell(r-1,c)
                addcell(r,c+1)
                addcell(r,c-1)

            distance += 1
        
        