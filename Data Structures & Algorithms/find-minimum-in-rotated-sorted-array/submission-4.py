class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums)-1

        minval = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                minval = min(minval, nums[l])
                break

            m = ((r+l)//2)
            minval = min(minval, nums[m])
            if nums[m] < nums[r]:
                r = m-1
            else:
                l = m + 1
        return minval
