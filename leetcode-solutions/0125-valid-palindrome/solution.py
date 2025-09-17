class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # Skip non-alphanumeric from left
            if not s[l].isalnum():
                l += 1
                continue

            # Skip non-alphanumeric from right
            if not s[r].isalnum():
                r -= 1
                continue
                
            # Compare after converting to lowercase
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        
        return True

