class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while stones:
            if len(stones) == 1:
                break
    
            first = -1 * heapq.heappop(stones)
            second = -1 * heapq.heappop(stones)

            if first > second:
                first = first - second
                heapq.heappush(stones, -1 * first)
            
            elif first < second:
                second = second - first 
                heapq.heappush(stones, -1 * second)
            
        if stones: 
            return (-1 * stones[0])
        else:
            return 0

                