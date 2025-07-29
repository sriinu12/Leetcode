# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        curr = root

        while curr:
            if not curr.left:
                # no left subtree → visit and go right
                result.append(curr.val)
                curr = curr.right
            else:
                # find predecessor (rightmost in left subtree)
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right

                if not pred.right:
                    # first time at curr: thread back, visit curr, go left
                    result.append(curr.val)
                    pred.right = curr
                    curr = curr.left
                else:
                    # second time at curr: remove thread, go right
                    pred.right = None
                    curr = curr.right

        return result