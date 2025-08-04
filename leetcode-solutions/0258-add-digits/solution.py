class Solution:
    def addDigits(self, num: int) -> int:
        """
        keep adding digits until we get a single digit
        38 -> 8 + 3 -> 11
        11 -> 1 + 1 -> 2 -> return
        """        
        while num > 9:
            sum = 0
            while num > 0:
                sum += (num % 10)
                num = (num // 10)
            
            num = sum
        return num
