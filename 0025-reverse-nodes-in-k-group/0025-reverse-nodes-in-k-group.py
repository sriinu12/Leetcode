# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Dummy node to simplify head manipulations
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Check if there are k nodes ahead
            kth = self._get_kth_node(group_prev, k)
            if not kth:
                break  # fewer than k nodes remain; done

            group_next = kth.next
            # Reverse this group
            prev, curr = kth.next, group_prev.next
            while curr is not group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Reattach reversed group
            tail = group_prev.next
            group_prev.next = kth
            group_prev = tail

        return dummy.next

    def _get_kth_node(self, start: ListNode, k: int) -> ListNode:
        """
        Return the k-th node after start (1-based), or None if fewer than k nodes remain.
        """
        curr = start
        for _ in range(k):
            curr = curr.next
            if not curr:
                return None
        return curr
        