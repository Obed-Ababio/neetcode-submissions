class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        n = len(heights)
        max_area = 0

        for i, height in enumerate(heights):
            start_idx = i
            while stack and stack[-1][0] > height:
                h, j = stack.pop()
                max_area = max(max_area, h * (i - j))
                start_idx = j
            stack.append((height, start_idx))
        
        while stack:
            h, j = stack.pop()
            max_area = max(max_area, h * (n - j))

        return max_area
        