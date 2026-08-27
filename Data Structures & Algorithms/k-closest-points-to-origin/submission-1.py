class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        res = []

        for i in range(len(points)):
            x = points[i][0] ** 2
            y = points[i][1] ** 2
            total = x + y
            res.append((total, points[i]))
        
        res = [(-p[0], p[1]) for p in res]
        heapq.heapify(res)

        while len(res) > k: 
            heapq.heappop(res)

        final = []
        for i in range(len(res)):
            final.append(res[i][1])
        
        return final
            



