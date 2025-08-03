# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = deque([(root, 1)])  # pair of (node, index)
        
        while queue:
            level_size = len(queue)
            # Indices at this level
            first_idx = queue[0][1]
            last_idx  = queue[-1][1]
            # width is inclusive
            max_width = max(max_width, last_idx - first_idx + 1)
            
            for _ in range(level_size):
                node, idx = queue.popleft()
                # Assign children their "virtual" indices
                if node.left:
                    queue.append((node.left,  idx * 2))
                if node.right:
                    queue.append((node.right, idx * 2 + 1))
        
        return max_width
        