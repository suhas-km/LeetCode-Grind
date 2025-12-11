class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        path = []

        def backtrack(i):
            if i == n:
                res.append(path.copy())  # <-- call .copy()
                return
            
            # choice 1: don't include nums[i]
            backtrack(i + 1)

            # choice 2: include nums[i]
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

        backtrack(0)   # <-- start recursion
        return res     # <-- return result

