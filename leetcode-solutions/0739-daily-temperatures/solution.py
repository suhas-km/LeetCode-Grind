class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing order - retriving a result in linear time!
        res = [0] * len(temperatures)
        stck = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stck and t > stck[-1][0]:
                stckT, stckInd = stck.pop()
                res[stckInd] = (i - stckInd)
            stck.append([t, i])

        return res
        
