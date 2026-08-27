class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.checker(nums[1:]),self.checker(nums[:-1]))



    def checker(self, nums):
        rob1, rob2 = 0,0
        for n in nums:
            temp = rob2
            rob2 = max(n+rob1, rob2)
            rob1 = temp
        
        return rob2