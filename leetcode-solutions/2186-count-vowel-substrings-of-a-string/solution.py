class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        j = 0
        count = 0
        vowels = {"a", "e", "i", "o", "u"}
        
        for i in range(len(word)):
            vowelCount = defaultdict(int)
            j = i
            
            while j < len(word) and word[j] in vowels:
                vowelCount[word[j]] += 1
                j += 1
                if len(vowelCount) == 5:
                    count += 1
        
        return count


