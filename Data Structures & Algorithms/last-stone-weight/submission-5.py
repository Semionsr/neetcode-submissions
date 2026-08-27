class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = - 1 * heapq.heappop(stones)
            second = -1 * heapq.heappop(stones)

            if second > first:
                second = -1 * (second - first)
                heapq.heappush(stones, second)
            elif second < first:
                first = -1 * (first - second)
                heapq.heappush(stones, first)
        
        if stones:
            return (-1 * stones[0])
        else:
            return 0


            
            