class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        max_area, L, R = 0, 0, n - 1

        while L < R:
            w = R -L
            h = min(heights[L], heights[R])
            a = w * h
            max_area = max(max_area, a)

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        
        return max_area
        