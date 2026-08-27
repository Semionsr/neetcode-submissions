class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        totalMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in totalMap:
                return [totalMap[diff], i]
            totalMap[n] = i
        return

        