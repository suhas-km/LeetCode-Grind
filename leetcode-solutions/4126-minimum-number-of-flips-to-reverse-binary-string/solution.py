class Solution:
    def minimumFlips(self, n: int) -> int:
        # Convert n to its binary representation string
        s = bin(n)[2:]  # [2:] to remove the "0b" prefix

        # Get the reverse of the binary string
        s_rev = s[::-1]

        flips = 0
        # Compare the original string with its reverse
        for i in range(len(s)):
            if s[i] != s_rev[i]:
                flips += 1
        
        return flips
        
