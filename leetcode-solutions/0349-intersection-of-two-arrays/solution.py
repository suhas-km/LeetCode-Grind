class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Ensure nums1 is the smaller list to optimize space
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Swap the lists
        
        # Now, nums1 is guaranteed to be the smaller or equal-sized list.
        lookup = set(nums1)
        result = set()
        
        for num in nums2:
            if num in lookup:
                result.add(num)
        
        return list(result)
