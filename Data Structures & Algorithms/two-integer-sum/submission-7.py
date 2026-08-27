class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in checker:
                return [checker[num],i]
            checker[nums[i]] = i