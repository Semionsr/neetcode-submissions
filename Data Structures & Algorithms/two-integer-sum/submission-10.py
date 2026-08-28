class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}


        for i in range(len(nums)):
            val = target - nums[i]
            if val in checker:
                return [checker[val], i]
            checker[nums[i]] = i
        
        return []