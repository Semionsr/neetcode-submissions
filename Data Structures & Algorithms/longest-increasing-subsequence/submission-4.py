class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # start at the end and then iterate backwards and see what numbers are less then that nuymber and then call that function again to see how many are larger
        LIS = [1] * len(nums)


        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)