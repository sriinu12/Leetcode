# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB
        
        # Continue until the two pointers either meet or both become None
        while pA is not pB:
            # Move pA to the next node or switch to headB if reaching end
            pA = pA.next if pA else headB
            # Move pB to the next node or switch to headA if reaching end
            pB = pB.next if pB else headA
        
        # They meet at the intersection node or at None
        return pA
        