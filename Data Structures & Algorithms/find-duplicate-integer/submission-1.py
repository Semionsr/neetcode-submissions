class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = 0

        slow, fast  = 0,0
        #checker for duplicates fast iterates twice as fast
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
