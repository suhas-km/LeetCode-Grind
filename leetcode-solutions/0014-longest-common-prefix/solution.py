from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        minLen = float("inf")

        for s in strs:
            if len(s) < minLen:
                minLen = len(s)
        
        i = 0
        while i < minLen:
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
            i += 1
        
        # edge case: Empty result
        return strs[0][:i]

