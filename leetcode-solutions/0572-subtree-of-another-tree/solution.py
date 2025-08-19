# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            
            if not root or not subRoot:
                return False
            
            if root.val == subRoot.val and sameTree(root, subRoot):
                return True

            left = dfs(root.left, subRoot)
            right = dfs(root.right, subRoot)

            return left or right
        
        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            
            if not root or not subRoot:
                return False
            
            if root.val != subRoot.val:
                return False
            
            left = sameTree(root.left, subRoot.left)
            right = sameTree(root.right, subRoot.right)

            return left and right

        return dfs(root, subRoot)
