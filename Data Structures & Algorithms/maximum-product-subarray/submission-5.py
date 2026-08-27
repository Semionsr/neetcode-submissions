class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = 0
        maxNum, minNum = 1,1

        if len(nums) == 1:
            return nums[0]


        for num in nums:
            temp = maxNum * num

            maxNum = max(maxNum * num, minNum * num, num)
            minNum = min(temp, minNum * num, num)
            res = max(res, maxNum)
        
        return res