class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # [1,2,3] -> 3 while last index is supposed to be 2

        def backtrack(subset, i):
            if i > len(nums) - 1:
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            left = backtrack(subset, i+1)
            subset.pop()
            right = backtrack(subset, i+1)
            # subset.pop()
    
            
        backtrack([], 0)

        return res

