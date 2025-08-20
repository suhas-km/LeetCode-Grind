# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(root, maxVal):
            nonlocal count
            if not root:
                return
            
            if root.val >= maxVal:
                count += 1
                maxVal = root.val
            
            left = dfs(root.left, maxVal)
            right = dfs(root.right, maxVal)
        
        dfs(root, root.val)
        
        return count
