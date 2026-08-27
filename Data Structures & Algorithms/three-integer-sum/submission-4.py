class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        j, k = 1, len(nums)-1
        res = set()
        nums.sort()



        for i in range(len(nums)):
            j = i + 1
            k = len(nums)-1
            target = -nums[i]

            while j < k:
                if target == nums[j] + nums[k]:
                    res.add((nums[i],nums[j],nums[k]))
                    j += 1
                    
                
                elif target < nums[j] + nums[k]:
                    k -= 1
                
                elif target > nums[j] + nums[k]:
                    j += 1
        
        return list(res)