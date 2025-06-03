# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Traverse both lists until both are exhausted
        while l1 or l2 or carry:
            # Get values (0 if list is already exhausted)
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Sum digits plus carry
            s = x + y + carry
            carry = s // 10          # New carry (1 or 0)
            digit = s % 10           # Digit to store in node
            
            # Append new node with the digit
            current.next = ListNode(digit)
            current = current.next
            
            # Advance l1 and l2 if possible
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return head of the resulting sum list
        return dummy.next
        