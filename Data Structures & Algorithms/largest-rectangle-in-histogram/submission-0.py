class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            prev_pop_idx = i
            while stack and stack[-1][0] > height:
                h, j = stack.pop()
                w = i - j
                a = h * w
                max_area = max(max_area, a)
                prev_pop_idx = j
            
            stack.append((height, prev_pop_idx))
        
        while stack:
            h, i = stack.pop()
            w = n - i
            a = h * w
            max_area = max(max_area, a)
        
        return max_area
            