class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for prime_number in [2, 3, 5]:
            while n % prime_number == 0:
                n = n // prime_number
        
        if n == 1:
            return True
        return False
