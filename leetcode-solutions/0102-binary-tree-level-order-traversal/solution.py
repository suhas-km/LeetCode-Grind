# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        dq = collections.deque()
        dq.append(root)

        while dq:
            subList = []
            for i in range(len(dq)):
                curr = dq.popleft()
                if curr:
                    subList.append(curr.val)
                    if curr.left:
                        dq.append(curr.left)
                    if curr.right:
                        dq.append(curr.right)
            if subList:
                res.append(subList)
        return res
