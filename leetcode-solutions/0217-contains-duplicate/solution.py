class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True
        
        # seen = set() #set of seen values

        # for i in nums:
        #     if i in seen:
        #         return True
        #     else:
        #         seen.add(i)
        
        # return False
