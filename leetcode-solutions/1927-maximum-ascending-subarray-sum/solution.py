from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        curr_sum = nums[0]  # Start with the first element
        
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:  # Continue the ascending sequence
                curr_sum += nums[i]
            else:
                max_sum = max(max_sum, curr_sum)  # Update max_sum
                curr_sum = nums[i]  # Start new sequence
        
        return max(max_sum, curr_sum)  # Ensure the last sequence is considered

