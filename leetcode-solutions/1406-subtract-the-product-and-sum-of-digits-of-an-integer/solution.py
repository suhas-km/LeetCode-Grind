class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        add = 0
        num_str = str(n)

        for i in num_str:
            prod *= int(i)
        
        for i in num_str:
            add += int(i)
        
        return prod - add
