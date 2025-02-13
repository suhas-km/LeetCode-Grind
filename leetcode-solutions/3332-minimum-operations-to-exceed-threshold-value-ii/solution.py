from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Convert the list into a min-heap.
        heapify(nums)
        count = 0
        
        # Continue while there are at least two elements 
        # and the smallest element is less than k.
        while len(nums) > 1 and nums[0] < k: # atleast length of 2 and minimum element is greater than k
            # Pop the two smallest numbers.
            x = heappop(nums)
            y = heappop(nums)
            
            # Combine them using the given formula:
            # Since x is the smaller (because it's a min-heap), 
            # the new value is 2*x + y.
            new_val = 2 * x + y
            
            # Push the combined value back into the heap.
            heappush(nums, new_val)
            
            # Increment the operation count.
            count += 1
        
        # If the smallest element is at least k, return count.
        # Otherwise, it was impossible to reach the threshold.
        return count if nums and nums[0] >= k else -1

