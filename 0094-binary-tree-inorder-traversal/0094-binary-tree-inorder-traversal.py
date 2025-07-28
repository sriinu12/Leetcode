# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        curr = root

        while curr:
            if not curr.left:
                result.append(curr.val)
                curr = curr.right
            else:
                # find predecessor
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right
                if not pred.right:
                    # link back to curr
                    pred.right = curr
                    curr = curr.left
                else:
                    # second visit: restore tree and visit
                    pred.right = None
                    result.append(curr.val)
                    curr = curr.right

        return result
        