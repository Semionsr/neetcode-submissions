class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total = [1]* len(nums)
        prefix = 1
        for i in range(len(nums)):
            total[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1,-1):
            total[i] *= postfix
            postfix *= nums[i]
        return total

