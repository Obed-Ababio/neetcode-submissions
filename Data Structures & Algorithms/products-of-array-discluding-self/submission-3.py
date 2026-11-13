class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        left_prod, right_prod = 1, 1
        left_arr, right_arr = [0] * n, [0] * n

        for i in range(n):
            j = -i - 1
            left_arr[i] = left_prod
            right_arr[j] = right_prod
            left_prod *= nums[i]
            right_prod *= nums[j]

        return [left_arr[i] * right_arr[i] for i in range(n) ]

