class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # r has to be greater then l b/c it is sorted in a nondecreasing order
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if target == total:
                return [l + 1,r + 1]
            elif  target < total:
                r -= 1
            elif  target > total:
                l += 1