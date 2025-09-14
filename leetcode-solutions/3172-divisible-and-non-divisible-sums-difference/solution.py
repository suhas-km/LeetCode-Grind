class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        n_str = str(n)
        m_str = str(m)

        num1 = 0
        num2 = 0

        for i in range(1, n + 1):
            if i % m != 0:
                num1 += i
        
        for i in range(1, n + 1):
            if i % m == 0:
                num2 += i
                
        return num1 - num2
