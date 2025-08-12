# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dq = deque([(p, q)])
        while dq:
            a, b = dq.popleft()
            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return False
            dq.append((a.left,  b.left))
            dq.append((a.right, b.right))
        return True
        