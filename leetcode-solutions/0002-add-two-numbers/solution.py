# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        mul = 1

        #342 = 2*1 + 4*10 + 3*100
        while l1 or l2:
            if l1:
                num1 += l1.val * mul
                l1 = l1.next
            if l2:
                num2 += l2.val * mul
                l2 = l2.next
            mul *= 10
        
        total = num1 + num2
        dummy = ListNode()
        head = dummy

        if total == 0:
            return ListNode(0)

        while total > 0:
            currDigit = total % 10 #to get the last digit
            total = total // 10 #to remove the last digit
            dummy.next = ListNode(currDigit)
            dummy = dummy.next
        
        

        return head.next
