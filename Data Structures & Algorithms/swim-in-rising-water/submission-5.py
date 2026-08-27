class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]  # (time/max-height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minH:
            t,r,c = heapq.heappop(minH)
            if r == N-1 and c == N-1:
                return t
            
            
            
            for dr,dc in directions:
                rows, cols = r+dr, c + dc

                if (rows < 0 or cols < 0 or rows >= N or cols >= N or
                    (rows,cols) in visit):
                    continue
                visit.add((rows,cols))
                heapq.heappush(minH, [max(t, grid[rows][cols]), rows, cols])


