class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # returing atleast the maximum and avoid returning 0
        curMax, curMin = 1, 1 # neutral value
        
        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1 # resetting the values to avoid returning 0 as the product
                continue
                
            tmp = curMax * n # we do this to use the old curMax i.e. from the previous loop and use it to find curMin
            curMax = max(n * curMax, n * curMin, n) # multiplying n with both maxuimums and minimums to find the max
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        
        return res
