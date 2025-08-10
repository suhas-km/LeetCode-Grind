class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        total = 0

        def backtrack(combination, i):
        # base case update the total to 0
            nonlocal total
            if total == target:
                res.append(combination.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            combination.append(candidates[i])
            total += candidates[i]
            backtrack(combination, i)
            combination.pop()
            
            total -= candidates[i]
            backtrack(combination, i + 1)
            # combination.pop()
            
        backtrack([], 0)
        return res
