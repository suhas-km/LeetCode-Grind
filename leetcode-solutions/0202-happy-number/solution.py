class Solution:
    def isHappy(self, n: int) -> bool:
        # use set() to keep track and findout if the sum of squares of digit

        # slow and fast also we can do

        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
        
        return False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        
        return output
