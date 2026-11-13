class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for anagram in strs:
            anagram_key = tuple(sorted(anagram))
            anagram_dict[anagram_key].append(anagram)
        return list(anagram_dict.values())