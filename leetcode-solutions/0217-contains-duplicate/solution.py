class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for num in nums:
            if(num in hashSet):
                return True
            hashSet.add(num)
        return False
        
        # Soltion 2 using while loop
        # seen = set()
        # num_len = len(nums)
        # count = 0

        # while count < num_len:
        #     if nums[count] in seen:
        #         return True
        #     seen.add(nums[count])
        #     count +=1
        # return False

