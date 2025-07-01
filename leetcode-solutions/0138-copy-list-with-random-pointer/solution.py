"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        realToCopy = { None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            realToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = realToCopy[cur]
            copy.next = realToCopy[cur.next]
            copy.random = realToCopy[cur.random]
            cur = cur.next

        return realToCopy[head]
