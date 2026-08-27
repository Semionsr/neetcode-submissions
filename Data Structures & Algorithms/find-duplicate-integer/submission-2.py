class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        new = 0
        while True:
            new = nums[new]
            slow = nums[slow]
            if new == slow:
                return slow
            
        return slow