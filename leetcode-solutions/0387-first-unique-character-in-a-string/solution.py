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

        # 1. Build a frequency count
        counts = collections.Counter(s)

        # 2. Find the first character with a count of 1
        for i, char in enumerate(s):
            if counts[char] == 1:
                return i

        return -1

