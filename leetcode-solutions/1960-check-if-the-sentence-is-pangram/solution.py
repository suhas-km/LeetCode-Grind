class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        chars = set()

        for ch in sentence:
            chars.add(ch)

        return len(chars) == 26
