class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        seen = set()

        for v in counter.values():
            if v in seen:
                return False
            else:
                seen.add(v)
        
        return True
