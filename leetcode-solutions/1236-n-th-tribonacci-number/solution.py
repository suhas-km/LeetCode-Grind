class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0

        if n == 1:
            return 1

        # if n == 2:
        #     return 2

        fib = [0, 1, 1]

        for i in range (3, n+1):
            fib.append(fib[i-1] + fib[i-2] + fib [i-3])

        return fib[n]
