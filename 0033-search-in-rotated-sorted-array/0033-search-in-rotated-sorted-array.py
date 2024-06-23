class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # Initialize pointers to the start and end of the array

        while l <= r:
            m = (l + r) // 2  # Calculate the middle index of the current subarray

            if nums[m] == target:
                return m  # If the target is found at the mid index, return the index

            # Check if the left half of the array is sorted
            if nums[l] <= nums[m]:
                # If the target is within the range of the sorted left half,
                # narrow the search to the left half by moving the right pointer
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    # Otherwise, search in the right half by moving the left pointer
                    l = m + 1
            else:
                # If the left half is not sorted, then the right half must be sorted
                # If the target is within the range of the sorted right half,
                # narrow the search to the right half by moving the left pointer
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    # Otherwise, search in the left half by moving the right pointer
                    r = m - 1

        return -1  # If the target is not found, return -1