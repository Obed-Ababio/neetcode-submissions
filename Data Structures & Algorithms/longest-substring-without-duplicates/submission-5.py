class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        best = 0
        count = {}
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        
        return best


        