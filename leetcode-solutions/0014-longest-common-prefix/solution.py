class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        reference = strs[0]
        res = ""

        for j in range(len(reference)):
            for i in range(1, len(strs)):
                s = strs[i]
                if j >= len(s) or s[j] != reference[j]:
                    return res

            res += reference[j]
        
        return res
        
