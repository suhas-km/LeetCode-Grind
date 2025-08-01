class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        
        for s in strs:
            key = [0] * 26
            for ch in s:
                key[ord(ch) - ord("a")] += 1
            anagram[tuple(key)].append(s)

        res = []

        for _, value in anagram.items():
            res.append(value)

        return res
