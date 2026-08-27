class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = set()

        for i in range(len(nums)):
            if checker and nums[i] in checker:
                return True
            checker.add(nums[i])
        return False