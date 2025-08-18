class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for ch in word:
                key[ord(ch) - ord("a")] += 1
            
            anagrams[tuple(key)].append(word)
        
        res = []
        for _, value in anagrams.items():
            res.append(value)
        
        return res
