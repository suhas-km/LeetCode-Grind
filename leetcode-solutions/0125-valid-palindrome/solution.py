class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        
        for c in s:
            if c.isalnum(): #  alphanumeric-> i.e. letters (a-z, A-Z) or numbers (0-9). 
                            # If string contains only alphanumeric characters and is not empty, isalnum() returns True
                newStr += c.lower()
        return newStr == newStr[::-1]
