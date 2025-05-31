# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        # Advance fast by two and slow by one until fast reaches the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow now points to the middle (second middle when even length)
        return slow
        