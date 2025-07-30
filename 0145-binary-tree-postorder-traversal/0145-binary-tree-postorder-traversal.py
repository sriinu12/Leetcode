# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        s1, s2 = [root], []
        while s1:
            node = s1.pop()
            s2.append(node.val)
            # Push children: left first, right next
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        # s2 has “root → right → left” order, so reverse it
        return s2[::-1]
        