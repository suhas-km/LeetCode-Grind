class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hmS = {}
        hmT = {}

        for i in range(len(s)):
            
            if s[i] not in hmS:
                hmS[s[i]] = i

            if t[i] not in hmT:
                hmT[t[i]] = i
        
        for i in range(len(s)):
            if hmS[s[i]] != hmT[t[i]]:
                return False
        
        return True
