class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd, postfixProd = 1, 1
        n = len(nums)
        res = [1] * n

        for i in range(len(nums)): #prefixProd
            res[i] = prefixProd
            prefixProd *= nums[i]
        
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfixProd
            postfixProd *= nums[i]
        
        return res
