class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26

        for c1 in s:
            freq[ord(c1) - ord('a')] += 1
        
        for c2 in t:
            freq[ord(c2) - ord('a')] -= 1
        
        for st in freq:
            if st != 0:
                return False
        
        return True
        
