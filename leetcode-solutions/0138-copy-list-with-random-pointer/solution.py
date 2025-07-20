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
        
        # pass 1: create the nodes values in the hashmap
        while cur:
            copy = Node(cur.val)
            realToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        #pass 2: connect deepcopy to next and random
        while cur:
            copy = realToCopy[cur]
            copy.next = realToCopy[cur.next]
            copy.random = realToCopy[cur.random]
            cur = cur.next
        
        return realToCopy[head]
