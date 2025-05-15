class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # hashmap for seen values to find in o(1)\
        
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return i, seen[remaining]
            else:
                seen[value] = i

