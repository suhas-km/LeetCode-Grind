class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        example: hook
        hashset - for 0(1) lookup and seen charecters
        store the index as well along with charecter

        seen = {h: [0, 1], o: [1, 2], k: [3, 1]} -> key(char): [firstIndex, Count]
        v == 1, to retrieve the first non-repeating element - o(N)
        
        Time: O(N)
        Space: O(1) -> max size of hashmap is numbers of alphabets regardless of input size
        """

        seen = {}

        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]][1] += 1
            else:
                seen[s[i]] = [i, 1]
        
        for _, value in seen.items():
            if value[1] == 1:
                return value[0]
        
        return -1
