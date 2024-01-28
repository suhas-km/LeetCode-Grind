class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # using a set for efficient lookups
    
        for num in nums:  # iterate over elements of nums
            if num in seen:  # check if the element is in seen
                return True
            seen.add(num)  # add the element to seen

        return False
            
