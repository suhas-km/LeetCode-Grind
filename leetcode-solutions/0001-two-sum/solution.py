class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, value in enumerate(nums):

            complement = target - value

            if complement in seen:
                return [i, seen[complement]]
            
            else:
                seen[value] = i

        # O(n^2) Solution:

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):  # start at i+1 to avoid duplicate pairs
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

