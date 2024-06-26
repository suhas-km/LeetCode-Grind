make two passes, first in-order, second in-reverse, to compute products
​
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array with 1's. The length of the result array is the same as the input array.
        # The value 1 is used for initialization because it is the neutral element for multiplication.
        res = [1] * len(nums)
        
        # Initialize a variable to store the cumulative product of elements from the beginning of the array up to the current element.
        prefix = 1
        # Traverse the array from left to right. This loop calculates the product of all the elements before each index.
        for i in range(len(nums)):
            # Assign the cumulative product (prefix) up to the element before the current index to res[i].
            res[i] = prefix
            # Update the prefix by multiplying it with the current element, preparing it for the next index.
            prefix *= nums[i]
        
        # Initialize a variable to store the cumulative product of elements from the end of the array to the current element.
        postfix = 1
        # Traverse the array from right to left. This loop updates the result array by multiplying the prefix product (already stored in res) with the product of all elements after the current index.
        for i in range(len(nums) - 1, -1, -1):
            # Multiply the current value at res[i] (which holds the prefix product) with the current postfix value.
            # This operation gives the product of all elements except the current one.
            res[i] *= postfix
            # Update the postfix to include the current element, preparing it for the previous index in the next iteration.
            postfix *= nums[i]
        
        # Return the final result array where each element is the product of all other elements except itself.
        return res
