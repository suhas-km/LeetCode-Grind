class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        count = 0
        maxCount = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                count += 1
                maxCount = max(count, maxCount)
            
            else:
                count = 0
        
        return maxCount
