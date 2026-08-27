class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for r in range(len(heights)):
            start = r
            while stack and stack[-1][1] > heights[r]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (r - index))
                start = index
            stack.append((start,heights[r]))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
