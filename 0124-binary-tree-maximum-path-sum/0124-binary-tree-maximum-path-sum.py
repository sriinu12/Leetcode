from typing import Optional

# LeetCode's TreeNode
class TreeNode:
    def __init__(self, val: int = 0,
                 left: 'TreeNode' = None,
                 right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float('-inf')

        def gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left  = max(0, gain(node.left))   # ignore negative paths
            right = max(0, gain(node.right))
            # Path that bends at node (could be global best)
            self.best = max(self.best, node.val + left + right)
            # Gain contributed to parent: choose one side
            return node.val + max(left, right)

        gain(root)
        return self.best
