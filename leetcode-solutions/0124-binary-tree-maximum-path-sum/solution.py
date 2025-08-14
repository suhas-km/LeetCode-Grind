# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxValue = float("-inf")

        def dfs(root):
            nonlocal maxValue
            if not root:
                return 0
            
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            maxValue = max(maxValue, left + right + root.val)
            return max(left, right) + root.val
        
        dfs(root)

        return maxValue 
        
