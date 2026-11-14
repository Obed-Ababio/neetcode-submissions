class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        best = 0
        window = {}

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            while ( r - l + 1 - max(window.values())) > k:
                window[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        
        return best
        