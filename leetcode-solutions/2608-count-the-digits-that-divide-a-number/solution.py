class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        number = num

        while num > 0:
            digit = num % 10

            if number % digit == 0:
                count += 1

            num = num // 10 # removes the last digit - post remainder calc
        
        return count
