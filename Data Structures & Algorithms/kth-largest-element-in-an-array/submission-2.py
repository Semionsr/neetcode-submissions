class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #nums = [-n for n in nums]
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        return (nums[0])