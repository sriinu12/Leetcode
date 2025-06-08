# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # 1) Find middle (end of first half)
        first_half_end = self._end_of_first_half(head)
        # 2) Reverse second half
        second_half_start = self._reverse_list(first_half_end.next)
        
        # 3) Check palindrome
        p1, p2 = head, second_half_start
        result = True
        while result and p2:  # only need to compare until p2 is exhausted
            if p1.val != p2.val:
                result = False
            p1 = p1.next
            p2 = p2.next
        
        # 4) Optional: restore the list
        first_half_end.next = self._reverse_list(second_half_start)
        
        return result

    def _end_of_first_half(self, head: ListNode) -> ListNode:
        """
        Uses fast & slow pointers: fast moves 2 steps, slow moves 1.
        When fast reaches end (or fast.next is None), slow is at the end of the first half.
        """
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _reverse_list(self, head: ListNode) -> ListNode:
        """
        Standard in-place reversal of a singly linked list.
        """
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        