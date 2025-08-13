# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        return none if no intersection

        """

        lenA = 0
        lenB = 0
        currA, currB = headA, headB

        while currA or currB:
            if currA:
                lenA += 1 
                currA = currA.next
            
            if currB:
                lenB += 1 
                currB = currB.next
        print(lenA)
        print(lenB)
        
        diff = abs(lenA - lenB)

        if lenA >= lenB:
            while diff > 0:
                headA = headA.next
                diff -= 1

        else:
            while diff > 0:
                headB = headB.next
                diff -= 1
        
        while headA and headB:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next
        
        return None
