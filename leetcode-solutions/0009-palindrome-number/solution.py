class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Handle negative numbers immediately as they can't be palindromes (unless specifically defined otherwise)
        if x < 0:
            return False

        num_str = str(x)  # Convert the integer to a string
        l = 0
        r = len(num_str) - 1

        while l <= r:
            if num_str[l] == num_str[r]:  # Access characters from the string
                l += 1
                r -= 1
            
            else: 
                return False
        
        return True
