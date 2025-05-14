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
# Purpose: The function deleteDuplicates removes all nodes with duplicate values from a sorted linked list, leaving only nodes with unique values.

# Dummy Node: A dummy node (dummy) is created and linked to the head of the list to simplify edge-case handling, such as removing duplicates at the start of the list.

# Pointers:

    # prev: Tracks the last node before the current block of duplicates.
    # cur: Iterates through the list to detect and handle duplicates.
# Detecting Duplicates:

    # If cur.next exists and cur.val == cur.next.val, the current node is part of a duplicate block.
# Skipping Duplicates:

    # The value of the duplicate (dup_val) is stored.
    # A while loop skips all nodes with the value dup_val, effectively removing the entire block of duplicates.
# Linking Around Duplicates:

    # After skipping duplicates, prev.next is updated to point to the first non-duplicate node (cur), bypassing the duplicate block.
# Handling Unique Nodes:

    # If the current node is unique, prev is moved to cur, and cur advances to the next node.
# Return Value:

    # The function returns dummy.next, which points to the head of the modified list.
# Edge Cases:

    # Handles empty lists (head = None) and lists with all duplicate or all unique values.
# Time Complexity:

    # O(n), where n is the number of nodes in the list, as each node is visited once.
    # Space complexity is O(1) since no additional data structures are used.
