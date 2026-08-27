class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}

        for i, n in enumerate(nums):
            total = target - n 
            if total not in output:
                output[n] = i
            else:
                return [output[total], i]
