class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        count = 0
        j = 0

        for i in range(len(word)):
            vowelCount = defaultdict(int) # because ne wslide starts
            j = i # use j to keep loop in bound

            while j < len(word) and word[j] in vowels:
                vowelCount[word[j]] += 1
                j += 1
                if len(vowelCount) == 5:
                    count += 1
                    
        return count
