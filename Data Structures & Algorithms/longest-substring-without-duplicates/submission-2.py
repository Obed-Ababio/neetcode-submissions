class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        dup_set = set()
        l = 0
        r = 0
        longest_substr = 0

        for i in range(n):
            while s[r] in dup_set:
                dup_set.remove(s[l])
                l += 1
            w = (r - l) + 1
            longest_substr = max(longest_substr, w)
            dup_set.add(s[r])
            r += 1

        return longest_substr