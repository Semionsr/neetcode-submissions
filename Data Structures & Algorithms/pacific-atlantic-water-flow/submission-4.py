class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()

        
        
        def dfs(r,c,checker,prevHeight):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                heights[r][c] < prevHeight or (r,c) in checker):
                return
            checker.add((r,c))
            prevHeight = heights[r][c]
            dfs(r+1,c,checker,prevHeight)
            dfs(r-1,c,checker,prevHeight)
            dfs(r,c+1,checker,prevHeight)
            dfs(r,c-1,checker,prevHeight)

        
        
        
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])


        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append((r,c))
        
        return res
        

