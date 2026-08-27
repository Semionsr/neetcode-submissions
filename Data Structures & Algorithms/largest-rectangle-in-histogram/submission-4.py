class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                stackind, stackheight = stack.pop()
                res = max(res, stackheight * (i - stackind))
                start = stackind
            stack.append((start, heights[i]))
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        return res
