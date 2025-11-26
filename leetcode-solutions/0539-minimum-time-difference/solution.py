class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort() #n* log n

        def time_to_min(t):
            h, m = map(int, t.split(":"))
            total = h * 60 + m
            return total
        
        # assign res to max:
        res = (24 * 60 - time_to_min(timePoints[-1]) + time_to_min(timePoints[0]))

        for time in range(len(timePoints) - 1):
            cur = time_to_min(timePoints[time + 1])
            prev = time_to_min(timePoints[time])
            diff = cur - prev
            res = min(res, diff)
        
        return res
