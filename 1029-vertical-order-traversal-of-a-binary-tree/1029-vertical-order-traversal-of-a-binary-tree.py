# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # Map column index -> list of (row, value)
        col_table = defaultdict(list)
        
        # DFS helper to record (row, col, val)
        def dfs(node: TreeNode, row: int, col: int):
            if not node:
                return
            col_table[col].append((row, node.val))
            dfs(node.left,  row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        
        # Populate the table
        dfs(root, row=0, col=0)
        
        # Build output by sorting columns and their contents
        result = []
        for col in sorted(col_table.keys()):
            # sort by row ascending, then val ascending
            col_entries = sorted(col_table[col], key=lambda x: (x[0], x[1]))
            # extract only the values
            column_vals = [val for _, val in col_entries]
            result.append(column_vals)
        
        return result
        