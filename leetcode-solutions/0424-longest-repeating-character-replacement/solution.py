class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        max_count = 0  # Max freq of any char in the window
        left = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])

            # If more than k replacements needed, shrink window
            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            # Update result with window size
            res = max(res, right - left + 1)

        return res

