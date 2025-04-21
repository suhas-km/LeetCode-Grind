class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # keep map of seen values.

        for i, value in enumerate(nums):

            remaining = target - nums[i] # x + y = z

            if remaining in seen:
                return i, seen[remaining]
            else:
                seen[value] = i #seen.add(i)
                continue
