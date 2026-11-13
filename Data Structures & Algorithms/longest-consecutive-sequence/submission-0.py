class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)

        longest = 0
        

        for num in nums:
            streak = 0
            curr = num
            if num - 1 not in num_set:
                while curr in num_set:
                    streak += 1
                    curr += 1
            longest = max(longest, streak)
        
        return longest
                
        