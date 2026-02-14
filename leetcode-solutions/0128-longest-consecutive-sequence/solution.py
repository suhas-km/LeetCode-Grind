class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert to set once
        numsSet = set(nums)
        maxlen = 0

        # FIX: Iterate over the SET, not the LIST
        for num in numsSet:
            if (num - 1) not in numsSet:
                curlen = 1 # Start at 1
                while (num + curlen) in numsSet:
                    curlen += 1
                
                if curlen > maxlen:
                    maxlen = curlen
        
        return maxlen
