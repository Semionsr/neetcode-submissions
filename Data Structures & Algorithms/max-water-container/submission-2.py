class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            new_res = 0
            if heights[l] > heights[r]:
                distance = r - l
                new_res = distance * heights[r]
                r -= 1
            elif heights[l] <= heights[r]:
                distance = r - l
                new_res = distance * heights[l]
                l += 1
            
            if new_res > res:
                res = new_res
        return res
            