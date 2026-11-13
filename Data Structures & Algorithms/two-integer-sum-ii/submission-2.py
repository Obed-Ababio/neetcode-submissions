class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        L = 0
        R = n - 1

        while L < R:
            summ =  numbers[L] + numbers[R]

            if summ == target:
                return [L + 1, R + 1]
            elif summ < target:
                L += 1
            else:
                R -= 1