class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        maxlen = 0
        
        for n in nums:
            if n - 1 not in set1: # make sure its starting point
                curlen = 0
                while n + curlen in set1:
                    curlen += 1
                maxlen = max(maxlen, curlen)
        return maxlen
'''
The space complexity of this algorithm is O(n), since we store all of the elements in the input list in a set.

The time complexity of this algorithm is O(n), since we iterate over the entire input list once and we perform a constant number of operations on each element.
'''
