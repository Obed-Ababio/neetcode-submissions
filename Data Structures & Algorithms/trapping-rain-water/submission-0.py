class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        max_l, max_r = 0, 0
        left_arr, right_arr = [0] * n, [0] * n

        for i in range(n):
            j = -i - 1

            left_arr[i] = max_l
            right_arr[j] = max_r
            max_l = max(max_l, height[i])
            max_r = max(max_r, height[j])
        
        total_wtr = 0

        for i in range(n):
            if i == 0 or i == n - 1:
                continue
            
            potential_wtr = (min(left_arr[i], right_arr[i]) - height[i])

            if potential_wtr > 0:
                total_wtr += potential_wtr
        
        return total_wtr

        