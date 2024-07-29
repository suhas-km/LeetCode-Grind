class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        diff = [nums2[i] - nums1[i] for i in range(len(nums1))]
        x = sum(diff) // len(diff)
        return x