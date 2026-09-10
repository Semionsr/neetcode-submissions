class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Brute force: sorting the initial function
        # after sorting the function use the k as counter ands iterate from the end of the array to the front
        # so for example nums = [2,3,1,5,4], k = 2

        nums.sort()

        for i in range(len(nums)-1,-1,-1):
            if k == 1:
                return nums[i]
            k-=1
        
        