class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = ""
        for char in s.lower():
            if char.isalnum():
                string += char
        
        reverse_string = string[::-1]
        print(string)
        print(reverse_string)

        return string == reverse_string
