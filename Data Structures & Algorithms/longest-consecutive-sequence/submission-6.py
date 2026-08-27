class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        res = 1
        count = 0

        total = set(nums)

        for i in range(len(nums)):
            if nums[i] - 1 not in total:
                count = 1
                while (nums[i] + count) in total:
                    count += 1
                res = max(res, count)
            
        
        return res
             
        