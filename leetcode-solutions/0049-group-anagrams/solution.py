class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # a hashmmap to group similar keys 
        # keys - alphabeical represntation of the word we are currently seeing
        anagrams = defaultdict(list)
        res = []

        for word in strs:
            key = [0] * 26
            for ch in word:
                key[ord(ch) - ord("a")] += 1

            anagrams[tuple(key)].append(word)

        for _, value in anagrams.items():
            res.append(value)
        
        return res
