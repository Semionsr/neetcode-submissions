class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        suf = 1
        nums2 = nums.copy()

        for i in range(len(nums)):
            tmp = nums[i]
            nums[i] = pre
            pre *= tmp

        for i in range(len(nums)-1,-1,-1):
            nums[i] = suf * nums[i]

            suf *= nums2[i]

        
        return nums