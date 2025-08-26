class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # # monotonic decreasing order - retriving a result in linear time!
        
        answer = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                answer[stackInd] = i - stackInd
            stack.append([t, i])
        
        return answer
