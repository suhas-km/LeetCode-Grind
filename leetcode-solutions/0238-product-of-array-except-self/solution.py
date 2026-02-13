class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd, suffixProd = 1, 1
        n = len(nums)
        res = [1] * n

        for i in range(n):
            res[i] = prefixProd
            prefixProd *= nums[i]
        
        for i in range(n - 1, -1, -1):
            res[i] *= suffixProd
            suffixProd *= nums[i]
        
        return res
