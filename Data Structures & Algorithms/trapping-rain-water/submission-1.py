class Solution:
    def trap(self, height: List[int]) -> int:
       
        L, R = 0, len(height) - 1
        max_l, max_r = height[L], height[R]
        water = 0

        while L <= R:
            if max_l < max_r:
                water += max(0, max_l - height[L])
                max_l = max(max_l, height[L])
                L += 1
            else:
                water += max(0, max_r - height[R])
                max_r = max(max_r, height[R])
                R -= 1
        return water