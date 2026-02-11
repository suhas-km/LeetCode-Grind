class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        t = sorted(t)
        s = sorted(s)

        return t == s

        # time: O(n logn)
        # space: O(n)
