"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}                 # {old_node: new_node}
        q = collections.deque([node])
        oldToNew[node] = Node(node.val)  # create clone for the start node

        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)  # create clone when first seen
                    q.append(nei)
                # connect cloned current -> cloned neighbor
                oldToNew[curr].neighbors.append(oldToNew[nei])

        return oldToNew[node]
