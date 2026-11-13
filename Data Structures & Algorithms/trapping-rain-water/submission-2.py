class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        L, R = 0, n - 1
        max_L, max_R = height[L], height[R]
        water = 0

        while L < R:
            if max_L < max_R:
                L += 1
                water += max(0, max_L - height[L])
                max_L = max(max_L, height[L])
            else:
                R -= 1
                water += max(0, max_R - height[R])
                max_R = max(max_R, height[R])
        return water
                
        