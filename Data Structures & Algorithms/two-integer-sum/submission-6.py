class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in checker:
                return [checker[difference], i]
            checker[nums[i]] = i