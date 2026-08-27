class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        total = 0

        while l < r:
            bottom = r - l
            current = min(heights[l], heights[r]) * bottom
            total = max(current, total)
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1
        
        return total

