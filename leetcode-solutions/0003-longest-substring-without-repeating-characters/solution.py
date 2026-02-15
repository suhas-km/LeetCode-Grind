class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        dedupS = set()
        l = 0

        for r in range(len(s)):
            while s[r] in dedupS:
                dedupS.remove(s[l])
                l += 1
            maxLen = max(maxLen, (r - l) + 1)

            dedupS.add(s[r])
        
        return maxLen


