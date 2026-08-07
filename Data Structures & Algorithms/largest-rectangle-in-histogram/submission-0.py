class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        heights.append(0)
        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                left = stack[-1] if stack else -1
                area = heights[index] * (i - left - 1)
                maxArea = max(maxArea, area)

            stack.append(i)
        return maxArea