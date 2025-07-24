# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Recursive check: both nodes must be present, hold the same value,
# and their corresponding sub-trees must also be identical.
# Recursive check: both nodes must be present, hold the same value,
# and their corresponding sub-trees must also be identical.
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:          # both empty → same
            return True
        if not p or not q:           # one empty, one not → different
            return False
        if p.val != q.val:           # values differ → different
            return False
        # recurse on left and right children
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


# If you prefer a standalone function ☟
def solution(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return solution(p.left, q.left) and solution(p.right, q.right)

