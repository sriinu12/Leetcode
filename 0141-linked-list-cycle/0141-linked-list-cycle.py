# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next         # move slow by 1
            fast = fast.next.next    # move fast by 2
            if slow is fast:
                return True         # cycle detected
        
        return False                # fast reached the end (no cycle)
        