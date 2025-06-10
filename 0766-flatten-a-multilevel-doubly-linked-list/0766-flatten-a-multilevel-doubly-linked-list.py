"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        # Dummy node to simplify edge cases
        dummy = Node(0)
        dummy.next = head
        head.prev = dummy
        
        stack = []
        curr = head
        
        while curr:
            # If there's a child, we need to splice it in
            if curr.child:
                # If there's a next node, push it onto the stack
                if curr.next:
                    stack.append(curr.next)
                    curr.next.prev = None  # detach for now
                
                # Connect curr to child list
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            
            # If no next but saved nodes remain, pop one and attach
            if not curr.next and stack:
                nxt = stack.pop()
                curr.next = nxt
                nxt.prev = curr
            
            # Move forward in the now-linear list
            curr = curr.next
        
        # Detach dummy and fix head.prev
        head = dummy.next
        head.prev = None
        return head
        