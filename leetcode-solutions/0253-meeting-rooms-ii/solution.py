class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Min-heap to store end times of meetings in progress
        # The top of the heap will always be the earliest ending meeting
        end_times_heap = []
        heapq.heappush(end_times_heap, intervals[0][1]) # Add the first meeting's end time

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            # If the current meeting starts after the earliest finishing meeting ends,
            # we can reuse that room (pop the old end time)
            if start >= end_times_heap[0]:
                heapq.heappop(end_times_heap)

            # Add the current meeting's end time (either reusing a room or needing a new one)
            heapq.heappush(end_times_heap, end)

        # The size of the heap at the end is the max number of concurrent meetings (rooms needed)
        return len(end_times_heap)

