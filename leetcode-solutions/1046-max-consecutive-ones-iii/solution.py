class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxx = 0 # track of max number of consecutive 1's
        num_zeros = 0
        
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0: # flip to 1 to test maxx?
                num_zeros += 1
            
            while num_zeros > k:
                if nums[l] == 0: # l's job to contract/shrink the window
                    num_zeros -= 1
                l += 1

            window = ((r - l) + 1)
            maxx = max(maxx, window) # update maxx after window resizing
        
        return maxx

        # time: 
        # space: 
