# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1) First, detect if a cycle exists by advancing slow by 1 and fast by 2.
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                # Cycle detected.
                break
        else:
            # No cycle: fast reached the end.
            return None

        # 2) To find the start of the cycle, reset one pointer to head,
        #    then move both one step at a time; they meet at the cycle start.
        ptr1 = head
        ptr2 = slow
        while ptr1 is not ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1
        