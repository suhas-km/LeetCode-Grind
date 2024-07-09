# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to help avoid edge cases
        dummy = ListNode()
        # Cur will keep track of the end of the merged list
        cur = dummy
        
        # Iterate while both list1 and list2 are not None
        while list1 and list2:
            # Compare the current nodes of both lists
            if list1.val < list2.val:
                # If the value in list1 is smaller, append it to the merged list
                cur.next = list1
                # Move to the next node in list1 and update cur to list1
                list1, cur = list1.next, list1
            else:
                # If the value in list2 is smaller or equal, append it to the merged list
                cur.next = list2
                # Move to the next node in list2 and update cur to list2
                list2, cur = list2.next, list2
        
        # If one of the lists is exhausted, append the remaining nodes of the other list
        if list1 or list2:
            cur.next = list1 if list1 else list2
        
        # Return the next node of dummy since dummy is a placeholder
        return dummy.next

