class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 'seen' will store the number as the key and its last seen index as the value.
        seen = {}

        for i in range(len(nums)):
            current_number = nums[i]
            
            # Check if we've seen this number before.
            if current_number in seen:
                # If seen, check if the distance between indices is within k.
                previous_index = seen[current_number]
                if i - previous_index <= k:
                    return True
            
            # Whether we found a duplicate or not, update the map with the current index.
            # This ensures we always have the most recent index for any number.
            seen[current_number] = i

        # If the loop completes, no such duplicate was found.
        return False
