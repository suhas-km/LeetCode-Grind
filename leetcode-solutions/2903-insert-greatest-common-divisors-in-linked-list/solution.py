# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head.next
        prev = head

        while cur:
            # find the gcd
            gcd = math.gcd(cur.val, prev.val)
            gcdNode = ListNode(gcd)
            # insert in between
            prev.next = gcdNode
            gcdNode.next = cur
            # move pointers
            prev = cur
            cur = cur.next
        
        return head
