class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Is this monotonically decreasing or increasing?
        res = [0] * len(temperatures)
        stack = []

        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                index, value = stack.pop()
                res[index] = abs(i - index)
            
            stack.append([i, v])
        
        return res
        
