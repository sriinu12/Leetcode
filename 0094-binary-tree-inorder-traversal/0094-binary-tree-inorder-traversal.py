# Definition for a binary tree node.
# class TreeNode:
    # def __init__(self, val=0, left=None, right=None):

    #     self.val = val
    #     self.left = left
    #     self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Return inorder traversal of a binary tree's nodes' values.
        Uses an explicit stack to simulate recursion.
        """
        result: List[int] = []
        stack: List[TreeNode] = []
        curr: Optional[TreeNode] = root

        while curr or stack:
            # Go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            # Process node
            curr = stack.pop()
            result.append(curr.val)
            # Then explore its right subtree
            curr = curr.right

        return result
        