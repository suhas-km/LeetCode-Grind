class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy()) # out of bound - base case
                return
            
            # decide the choose the val
            subset.append(nums[i])
            dfs(i + 1)

            # decided not to and go ahead
            subset.pop()
            dfs(i + 1)

        dfs(0) # 0th index
        return res

