class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
         # Append sentinel 0 to flush stack at the end
        heights.append(0)
        stack: List[int] = []
        max_area = 0
        
        for i, h in enumerate(heights):
            # While current bar is lower than the one on top of the stack
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                # Determine left boundary (index of previous smaller)
                left = stack[-1] if stack else -1
                # Width is from left+1 to i-1 inclusive
                width = i - left - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        # Clean up sentinel
        heights.pop()
        return max_area
        