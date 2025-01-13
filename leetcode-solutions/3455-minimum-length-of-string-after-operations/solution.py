class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        minus = 0
        
        # Iterate through character frequencies
        for x in count.values():
            # Repeatedly remove pairs of characters
            while x >= 3:
                minus += 2
                x -= 2
        
        # Subtract the removed characters from the original length
        return len(s) - minus

        # left, right = 0, len(s) - 1  # Two pointers at the start and end of the string
        
        # while left < right and s[left] == s[right]:
        #     char = s[left]  # Common character at the boundaries
            
        #     # Move the left pointer inward while the characters match `char`
        #     while left <= right and s[left] == char:
        #         left += 1
            
        #     # Move the right pointer inward while the characters match `char`
        #     while left <= right and s[right] == char:
        #         right -= 1
        
        # # The remaining substring length is `right - left + 1`
        # return right - left + 1


        # while True:
        #     # Check if there is any valid `i` to perform the operation
        #     found = False
        #     for i in range(1, len(s) - 1):  # Avoid out-of-bounds
        #         if s[i - 1] == s[i] and s[i + 1] == s[i]:
        #             # Remove the closest matching left and right characters
        #             left = i - 1
        #             right = i + 1
        #             s = s[:left] + s[right + 1:]
        #             found = True
        #             break  # Start over after modifying the string
        #     if not found:  # No valid operations left
        #         break
        # return len(s)

        # left, right = 0, len(s) - 1
