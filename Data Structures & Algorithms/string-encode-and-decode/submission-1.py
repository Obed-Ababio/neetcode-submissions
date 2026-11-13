class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for string in strs:
            res += str(len(string)) + '#' + string
        return res

    def decode(self, s: str) -> List[str]:
        
        res = []
        i = 0

        while i < len(s):

            str_len = ''
            while s[i] != '#':
                str_len += s[i]
                i += 1
            
            str_len = int(str_len)

            string = ''
            for j in range(i + 1, i + 1 + str_len):
                string += s[j]
            
            res.append(string)
            i = i + 1 + str_len
        
        return res



            

