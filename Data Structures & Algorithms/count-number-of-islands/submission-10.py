class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        q = collections.deque()
        islands = 0
        ROWS,COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    q.append([r,c])
                    grid[r][c] = '-1'
                    islands += 1
                    while q:
                        r, c = q.pop()
                        for dr,dc in directions:
                            rows, cols = dr + r, dc + c

                            if (rows < 0 or rows >= ROWS or cols < 0 or cols >= COLS or grid[rows][cols] == '-1' or grid[rows][cols] == '0'):
                                continue
                            q.append([rows,cols])
                            grid[rows][cols] = '-1'
        

        return islands
                            
                            


