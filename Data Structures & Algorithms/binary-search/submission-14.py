class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute Force Solution
        # Search through entire array and check for target
        # O(n) time O(1)
        
        
        #O(logn) Binary Search 

        l , r = 0, len(nums)
        

        while l < r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m+1
        

        return -1
                
