class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        res = []

        for word in strs:
            key = [0] * 26 #basically key for every word
            for ch in word:
                key[ord(ch) - ord("a")] += 1 # creating the key properly for thew word
            # appendd to anagrams
            anagrams[tuple(key)].append(word)
                
        for _, value in anagrams.items():
            res.append(value)
        
        return res
