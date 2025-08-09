from typing import Optional

# LeetCode's TreeNode
# class TreeNode:
#     def __init__(self, val: int = 0,
#                  left: 'TreeNode' = None,
#                  right: 'TreeNode' = None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Returns True if the binary tree is height-balanced.
        Bottom-up DFS: returns height if balanced, else -1.
        """
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            lh = dfs(node.left)
            if lh == -1:  # left subtree unbalanced
                return -1
            rh = dfs(node.right)
            if rh == -1:  # right subtree unbalanced
                return -1
            if abs(lh - rh) > 1:
                return -1
            return 1 + max(lh, rh)

        return dfs(root) != -1
