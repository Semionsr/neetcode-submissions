class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        #num_set == nums

        longest = 0
        for i in range(len(nums)):
            number = nums[i]
            
            if (number - 1) in num_set:
                continue
            else:
                res = 1
                while (number + res) in num_set:
                    res += 1
                
                longest = max(res, longest)
        return longest

