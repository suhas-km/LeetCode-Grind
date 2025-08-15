# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root):
            if not root:
                return None
            
            if p is root or q is root:
                return root
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if not left:
                return right
            
            if not right:
                return left
            
            if left and right:
                return root

        return dfs(root)


        

