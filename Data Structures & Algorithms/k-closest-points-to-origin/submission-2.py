class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x, y in points:
            total = -(x ** 2 + y ** 2)
            heapq.heappush(res, (total,x,y))
            if len(res) > k:
                heapq.heappop(res)

        total = []
        while res:
            dist, x, y = heapq.heappop(res)
            total.append([x, y])
        return total

