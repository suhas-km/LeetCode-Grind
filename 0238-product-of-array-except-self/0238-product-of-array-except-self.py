class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # Preparing the output Array
        
        
        prefix =1
        for i in range(len(nums)): # Starting loop to find the prefix values
            res[i] = prefix
            prefix *= nums[i] # Computing the Prefix value
            
            
        postfix = 1
        for i in range(len(nums) -1, -1, -1):# Starting from the end -> start of the list
            res[i] *= postfix # crucial, as we multiply the already calculated prefix values in res[i] with the new postfix values to finally output the result Product of Array Except Self.
            # Basically, we multiplied the Prefix and the Postfix together
            postfix *= nums[i] # we update the postfix continuosly as we should
        
        return res
            
            