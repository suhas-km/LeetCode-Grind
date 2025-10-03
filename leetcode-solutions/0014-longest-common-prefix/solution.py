from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Check each character of the first string against all other strings.
        for i, char in enumerate(strs[0]):
            for other_string in strs:
                # If a string is too short or its character doesn't match,
                # the common prefix ends here.
                if i == len(other_string) or other_string[i] != char:
                    return strs[0][:i]
        
        # If the loop finishes, the entire first string is the common prefix.
        return strs[0]
