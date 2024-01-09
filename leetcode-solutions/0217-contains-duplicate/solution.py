class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        i = 0

        while i < len(nums):
            if nums[i] in seen:
                return True
            else:
                seen[nums[i]] = True
            i += 1

        return False
                
