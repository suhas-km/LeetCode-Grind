class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        result = []

        # Find the maximum frequency of each character needed from words2
        max_freq = Counter()
        for i in words2:
            word_freq = Counter(i)
            for char in word_freq:
                max_freq[char] = max(max_freq[char], word_freq[char])

        for word in words1:
            word_freq = Counter(word)
            # i # If word_freq satisfies max_freq for all characters, add to result
            if all(word_freq[char] >= max_freq[char] for char in max_freq):
                result.append(word)
        
        return result
