class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit and move left
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                # If current digit is less than 9, just increment and return
                digits[i] += 1
                return digits
            else:
                # If digit is 9, it becomes 0, and carry goes to next digit
                digits[i] = 0

        # If all digits were 9, we need an extra digit at the front
        # e.g., 999 + 1 = 1000
        return [1] + digits
