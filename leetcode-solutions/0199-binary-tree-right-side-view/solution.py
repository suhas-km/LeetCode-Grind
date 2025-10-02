from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # We add a 'level' parameter to track the depth of each node.
        def dfs(node, level):
            if not node:
                return
            
            # The core idea: if the current level equals the size of our result list,
            # it means we are visiting this level for the first time. Since we
            # traverse right-first, this must be the right-most node at this level.
            if level == len(res):
                res.append(node.val)
            
            # 1. Traverse the right child first.
            dfs(node.right, level + 1)
            # 2. Then traverse the left child.
            dfs(node.left, level + 1)

        # Start the recursion from the root at level 0.
        dfs(root, 0)
        
        return res

