class Solution:
    def countKeyChanges(self, s: str) -> int:
        if not s:
            return 0

        changes = 0
        prev = s[0].lower()

        for ch in s[1:]:
            cur = ch.lower()
            if cur != prev:
                changes += 1
            prev = cur
            
        return changes

