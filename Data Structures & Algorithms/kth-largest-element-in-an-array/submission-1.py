class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        p = len(nums) - k
        while p > 0:
            heapq.heappop(nums)
            p-=1
        res = heapq.heappop(nums)
        return res


