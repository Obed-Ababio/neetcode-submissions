class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = []
        for val in nums:
            if val in cache:
                return True
            cache.append(val)
        return False
        