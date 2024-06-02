class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the most recent index of each value
        index_map = {}

        # Iterate over the list, using `i` as the index
        for i, value in enumerate(nums):
            if value in index_map:
        # Check if the current index and the stored index are within `k`distance
                if i - index_map[value] <= k:
                    return True
        # Update the dictionary with the most recent index of this value
            index_map[value] = i
        
        return False

