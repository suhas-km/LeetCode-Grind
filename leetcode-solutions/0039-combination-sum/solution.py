class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(i, total, subset):
            if total == target:
                res.append(subset.copy()) # cause: later pops will mutate saved solutions if not
                return
            if i == len(candidates) or total > target:
                return

            # left: pick candidates[i]
            subset.append(candidates[i])
            backtrack(i, total + candidates[i], subset)  # reuse same i
            subset.pop()

            # right: skip candidates[i]
            backtrack(i + 1, total, subset)

        backtrack(0, 0, [])
        return res

