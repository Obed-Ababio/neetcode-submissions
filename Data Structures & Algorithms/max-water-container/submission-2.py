class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        max_area = 0
        L = 0
        R = n - 1

        while L < R:
            w = R - L
            h = min(heights[R], heights[L])
            max_area = max(max_area, w * h)
    
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
            
        return max_area 
