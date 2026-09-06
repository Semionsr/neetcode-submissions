class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums)-1
            target = -nums[i]
            

            while j < k:
                if target == (nums[j]+nums[k]):
                    res.append([-target,nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                
                elif target < (nums[j]+nums[k]):
                    k -= 1
                
                else:
                    j += 1

        return res      

