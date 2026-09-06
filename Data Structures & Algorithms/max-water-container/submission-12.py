class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        maxw = 0

        while l < r:
            length = r - l

            minheight = min(heights[l],heights[r])
            maxw = max(maxw,length*minheight)

            if heights[r] < heights[l]:
                r -= 1
            
            else:
                l += 1
        
        return maxw