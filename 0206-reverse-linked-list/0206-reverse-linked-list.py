# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next   # temporarily store next node
            curr.next = prev  # reverse the link
            prev = curr       # move prev forward
            curr = nxt        # move curr forward
        
        # at end, prev is new head
        return prev

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        """
        Recursive reversal.
        Time: O(n), Space: O(n) due to call stack.
        """
        # base case: empty list or single node
        if not head or not head.next:
            return head
        
        # reverse rest of list
        new_head = self.reverseListRecursive(head.next)
        
        # head.next is now tail of reversed sublist
        head.next.next = head
        head.next = None
        
        return new_head