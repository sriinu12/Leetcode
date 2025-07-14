# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0
        node = head
        while node:
            # Shift previous bits left and add current bit
            res = (res << 1) | node.val
            node = node.next
        return res
        