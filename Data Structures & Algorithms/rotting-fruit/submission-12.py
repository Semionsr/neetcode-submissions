class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = collections.deque()
        fresh = 0
        time = 0


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        def addcell(r,c):
            nonlocal fresh
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                grid[r][c] != 1):
                return
            fresh -= 1
            grid[r][c] = 2
            q.append((r,c))

        
        while q and fresh > 0:
            qlen = len(q)
            #time = 0



            for i in range(qlen):
                r,c = q.popleft()
                addcell(r+1,c)
                addcell(r-1,c)
                addcell(r,c+1)
                addcell(r,c-1)
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1

        



