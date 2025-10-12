from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize trackers with the first element.
        res = nums[0]
        curMin, curMax = nums[0], nums[0]

        # Iterate from the second element.
        for n in nums[1:]:
            # When we see a negative number, the old max becomes the new min and vice versa.
            # We must store the old curMax to use it in the curMin calculation.
            old_curMax = curMax * n
            
            curMax = max(n, old_curMax, curMin * n)
            curMin = min(n, old_curMax, curMin * n)

            res = max(res, curMax)
        
        return res
