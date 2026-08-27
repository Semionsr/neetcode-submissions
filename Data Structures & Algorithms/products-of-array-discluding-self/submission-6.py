class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        checker1 = [0] * len(nums)

        num1 = 1
        for i in range(len(nums)):
            checker1[i] = num1
            num1 = nums[i] * num1

        num2 = 1
        for i in range(len(nums)-1, -1, -1):
            checker1[i] = checker1[i] * num2
            num2 = nums[i] * num2

        return checker1