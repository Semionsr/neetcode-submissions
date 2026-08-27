class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        
        heapq.heapify(stones)


        while stones and len(stones) > 1:
            first = -1 * heapq.heappop(stones)
            second = -1 * heapq.heappop(stones)

            if first > second:
                first = -1 * (first - second)

                heapq.heappush(stones, first)
            elif first < second:
                second = -1 * (second - first)

                heapq.heappush(stones, second)
        
        if stones:
            return -1 * stones[0]
        
        else:
            return 0
