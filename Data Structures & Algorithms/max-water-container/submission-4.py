class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            distance = r - l
            

            res = max(min(heights[l],heights[r]) * distance, res)
            print(min(heights[l], heights[r]) * distance)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
        
