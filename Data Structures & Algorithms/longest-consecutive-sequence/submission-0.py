class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        consecutive = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in numset:
                length = 0
                while (nums[i] + length) in numset:
                    length += 1
                    if length > consecutive:
                        consecutive = length
        return consecutive

