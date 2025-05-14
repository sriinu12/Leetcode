# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Remove all nodes that have duplicate values in a sorted list,
        leaving only nodes that appear exactly once.
        """
        # Dummy head to simplify edge-case removal at list start
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy  # the last node before the sublist of duplicates
        cur  = head
        
        while cur:
            # Detect duplicates by looking ahead
            if cur.next and cur.val == cur.next.val:
                dup_val = cur.val
                # Skip all nodes with this duplicated value
                while cur and cur.val == dup_val:
                    cur = cur.next
                # Link around the entire block of duplicates
                prev.next = cur
            else:
                # Current node is unique so far → move prev
                prev = cur
                cur  = cur.next
        
        return dummy.next
