class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                index, value = stack.pop()
                res[index] = abs(i - index)

            # append to stack if not
            stack.append([i, v])
        
        return res

