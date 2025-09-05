class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window, use R to expand and L to contract the window
        l = 0
        maxW = 0
        numZeros = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                numZeros += 1

            while numZeros > k:
                if nums[l] == 0:
                    numZeros -= 1
                l += 1
            
            w = r - l + 1
            maxW = max(w, maxW)
        
        return maxW
