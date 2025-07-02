class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()  # to track visited numbers

        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        
        return -1  # shouldn't happen, as per problem constraints

