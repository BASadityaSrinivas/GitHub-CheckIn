class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i,a in enumerate(heights):
            stack_min = i
            while stack and stack[-1][1] >= a:
                stack_min, stack_h = stack.pop()
                max_area = max(max_area, (i-stack_min) * stack_h)
            stack.append([stack_min, a])
        
        while stack:
            stack_min, stack_h = stack.pop()
            max_area = max(max_area, (len(heights) - stack_min) * stack_h)
        
        return max_area
