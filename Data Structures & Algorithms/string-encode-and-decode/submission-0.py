class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        print(f"encoded string: {s}")
        res = []
       
        
        i = 0
        while i < len(s):
            string_count = ''

            while s[i] != '#':
                string_count += s[i]
                i += 1
            
            word = ''
            checkpoint = 0
            for j in range(i + 1, i + int(string_count) + 1):
                word += s[j]
                checkpoint = j
            res.append(word)
            i = i + int(string_count) + 1
        return res
        
                



        