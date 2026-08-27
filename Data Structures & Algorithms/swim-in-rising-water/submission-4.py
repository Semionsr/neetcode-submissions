class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        N = len(grid)
        visit = set()
        visit.add((0, 0))
        minH = [[grid[0][0], 0, 0]]

        while minH:
            t,r,c = heapq.heappop(minH)
            if r == N -1 and c == N -1:
                return t
            for dr, dc in directions:
                rows = r + dr
                cols = c + dc

                if (rows < 0 or cols < 0 or rows >= N or cols >= N or (rows,cols) in visit):
                    continue
                
                visit.add((rows, cols))
                heapq.heappush(minH, [max(t,grid[rows][cols]),rows,cols])


