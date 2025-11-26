class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()

        def time_to_min(t):
            h, m = t.split(":")
            h, m = int(h), int(m)
            return 60 * h + m
        
        res = (
            24 * 60 -
            time_to_min(timePoints[-1]) +
            time_to_min(timePoints[0])
        ) # assigning it to maximum

        for i in range(len(timePoints) - 1):
            cur = time_to_min(timePoints[i + 1])
            prev = time_to_min(timePoints[i])
            diff = cur - prev
            res = min(res, diff)
            
        return res

