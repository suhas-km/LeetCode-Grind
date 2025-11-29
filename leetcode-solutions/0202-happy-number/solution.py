class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited: # if 
            visited.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
        
        return False

    def sumOfSquares(self, n):
        newN = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            newN += digit
            n = n // 10

        return newN

