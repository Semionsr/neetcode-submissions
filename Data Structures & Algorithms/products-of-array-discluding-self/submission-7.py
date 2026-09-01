class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        "1 1 2 8"
        "48 24 12 8"
        suffix = 1
        checker = nums.copy()

        for i in range(len(nums)):
            checker[i] = suffix
            suffix *= nums[i]
        
        prefix = 1
        for j in range(len(nums)-1,-1,-1):
            checker[j] *= prefix
            prefix *= nums[j]
        
        return checker

