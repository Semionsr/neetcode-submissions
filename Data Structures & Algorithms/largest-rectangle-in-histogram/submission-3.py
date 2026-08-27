class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        l = 0
        maxrect = 0
        

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                maxrect = max(height * (i-index), maxrect)
                start = index
            stack.append((start,heights[i]))
                
        for i, h in stack:
            maxrect = max(maxrect, h * (len(heights) - i))
        return maxrect
