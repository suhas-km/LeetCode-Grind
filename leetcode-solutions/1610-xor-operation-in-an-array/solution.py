class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []

        for i in range(0, n):
            nums.append(start + (2 * i))

        res = nums[0]

        for j in range(1, len(nums)):
            res ^= nums[j]

        return res
