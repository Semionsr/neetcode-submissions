class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #maxheap

        stones = [-n for n in stones]
        heapq.heapify(stones)

        for i in range(len(stones)-1):
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            val = -1 * abs(stone1-stone2)
            heapq.heappush(stones,val)
        
        return -1 * stones[0]
