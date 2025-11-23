class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubSum = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            
            curSum += num
            
            maxSubSum = max(maxSubSum, curSum)
        
        return maxSubSum
