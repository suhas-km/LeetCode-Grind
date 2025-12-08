class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        inserted = False

        for interval in intervals:
            # Case 1: interval is completely before newInterval → add it
            if interval[1] < newInterval[0]:
                result.append(interval)
            # Case 2: interval is completely after newInterval → time to insert
            elif interval[0] > newInterval[1]:
                if not inserted:
                    result.append(newInterval)
                    inserted = True
                result.append(interval)
            # Case 3: overlap → merge
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        # If never inserted (e.g., newInterval goes at end)
        if not inserted:
            result.append(newInterval)
            
        return result

