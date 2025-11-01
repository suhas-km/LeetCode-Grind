class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # 1 -> 0 - 30 -> False case for 2 -> 5
        prevEnd = float("-inf") # negetive because for an interval to be valid the prev end < the next meetings start
        intervals.sort()

        for interval in intervals:
            currentStart = interval[0]

            if not currentStart >= prevEnd:
                return False

            prevEnd = interval[1]
        
        return True

