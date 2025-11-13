class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        prefixLen = len(res)

        for string in strs[1:]:
            while string[0:prefixLen] != res:
                prefixLen -= 1
                if prefixLen == 0:
                    return ""
                
                res = res[0:prefixLen]

        return res
