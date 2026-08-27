class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        count = 1
        for i in range(len(nums)):
            prefix[i] = count
            count *= nums[i]

        count = 1
        count2 = 1
        for i in range(len(nums)-1,-1,-1):
            count = prefix[i] * count2
            count2 *= nums[i]
            suffix[i] = count
            

        return suffix