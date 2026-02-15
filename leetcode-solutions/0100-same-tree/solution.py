# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        elif not p or not q:
            return False
        
        elif p.val != q.val:
            return False

        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
    # have to get true for the left and the right subtree's of the root node
    
