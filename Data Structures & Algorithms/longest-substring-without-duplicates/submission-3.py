class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest_substr = 0
        dup_set = set()

        for i in range(len(s)):
            while s[r] in dup_set:
                dup_set.remove(s[l])
                l += 1

            w = r - l + 1
            longest_substr = max(longest_substr, w)
            dup_set.add(s[r])
            r += 1
        
        return longest_substr

        