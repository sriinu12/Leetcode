# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # This will hold the maximum diameter seen (in edges).
        self.ans = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            """
            Returns the height (in edges) of the subtree rooted at `node`,
            while updating self.ans with the largest diameter passing through `node`.
            """
            if not node:
                return 0
            left_height  = dfs(node.left)
            right_height = dfs(node.right)
            # Potential diameter at this node is the sum of left + right heights
            self.ans = max(self.ans, left_height + right_height)
            # Height of this subtree is 1 + max of child heights
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.ans
        