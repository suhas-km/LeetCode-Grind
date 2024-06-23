class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1  # Initialize pointers to the start and end of the array
        
        # Explanation: The given array is rotated, meaning it was originally sorted in ascending order and then rotated at some pivot.
        # The goal is to find the minimum element in this rotated sorted array.
        
        while l <= r:
            # If the subarray from l to r is already sorted, the smallest element is nums[l]
            if nums[l] < nums[r]: 
                res = min(res, nums[l])
                break
            
            # Calculate the middle index
            m = (l + r) // 2
            
            # Update the result with the minimum value found so far
            res = min(res, nums[m])
            
            # Determine which part of the array to search next
            if nums[m] >= nums[l]:
                # The left half is sorted, so the minimum must be in the right half
                l = m + 1
            else:
                # The right half is sorted, so the minimum must be in the left half
                r = m - 1
        
        return res
