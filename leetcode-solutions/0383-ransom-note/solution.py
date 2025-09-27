from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # This initial check is a great optimization.
        if len(ransomNote) > len(magazine):
            return False

        # Get character counts of the magazine.
        magazine_counts = Counter(magazine)

        # Check if the magazine has enough of each character needed for the note.
        for char in ransomNote:
            if magazine_counts[char] > 0:
                magazine_counts[char] -= 1  # Use up one character
            else:
                return False  # Not enough of this character available

        return True
