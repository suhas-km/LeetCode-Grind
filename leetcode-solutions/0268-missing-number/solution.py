class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        # FIX: Check each index against its expected value (0, 1, 2, ..., n-1)
        for i in range(len(nums)):
            if nums[i] != i:
                return i
                
        # FIX: If all elements match their indices, the missing number is n
        return len(nums)
