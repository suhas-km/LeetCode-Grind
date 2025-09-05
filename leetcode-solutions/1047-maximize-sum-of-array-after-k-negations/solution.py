class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # Sort by absolute value descending so the smallest |value| ends up last
        nums.sort(key=abs, reverse=True)

        # Flip negatives first (best gain per flip)
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        # If an odd flip remains, hit the smallest |value|
        if k % 2 == 1:
            nums[-1] = -nums[-1]

        return sum(nums)
