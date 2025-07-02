# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        mul = 1

        # num1 = 342 -> 3*100 + 4*20 + 2*1
        while l1 or l2:
            if l1:
                num1 += l1.val * mul
                l1 = l1.next
            if l2:  # changed from elif to if to allow both to contribute in same iteration
                num2 += l2.val * mul
                l2 = l2.next
            mul *= 10

        total = int(num1) + int(num2)

        dummy = ListNode()
        head = dummy

        if total == 0:
            return ListNode(0)

        while total > 0:
            currDigit = total % 10 #extract reminder
            total = total // 10 #remove digit - floor value
            
            dummy.next = ListNode(currDigit) #create node with reminder
            dummy = dummy.next

        return head.next

