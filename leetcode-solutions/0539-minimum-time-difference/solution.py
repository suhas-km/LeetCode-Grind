class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()

        def timeToMin(t):
            h, m = map(int, t.split(":"))
            # h, m = int(h), int(m)
            return h * 60 + m
        
        minDiff = (24 * 60 - timeToMin(timePoints[-1]) + timeToMin(timePoints[0]))

        for time in range(len(timePoints) - 1):
            cur = timeToMin(timePoints[time+1])
            prev = timeToMin(timePoints[time])
            diff = cur - prev
            minDiff = min(minDiff, diff)
        
        return minDiff

