# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] != nums[r]:
                return False
            
            l+=1
            r-=1
        return True
        
        
        
        # First create an empty array
        # While head is not None
        # Append the value of head to the array
        # Move the head to head.next
        # Now we have array of values of the link list
        # Declare left as 0 and right as length of array - 1
        # Using two pointer approach move from both end of the array by checking values are same or different
        # If it different break the loop
        # Return left >= Right
        