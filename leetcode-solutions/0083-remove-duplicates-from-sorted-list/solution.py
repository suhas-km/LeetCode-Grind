# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: # Base Case 
            return None
            
        current = head

        while current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            
            else:
                current = current.next
        
        return head
