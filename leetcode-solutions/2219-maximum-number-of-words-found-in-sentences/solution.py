class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        maxCount = 0

        for s in sentences:
            count = len(s.split(" "))
            maxCount = max(maxCount, count)
        
        return maxCount
