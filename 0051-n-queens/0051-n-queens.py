class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res: List[List[str]] = []
        
        # Track occupied columns and diagonals
        cols = set()
        diag1 = set()  # r - c
        diag2 = set()  # r + c
        
        board: List[str] = []  # current partial board, as list of strings
        
        def backtrack(r: int):
            # If we've placed queens on all rows, record a solution
            if r == n:
                res.append(board.copy())
                return
            
            # Try placing a queen in row r, each column c
            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue  # under attack, skip
                
                # Place queen at (r, c)
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                
                # Build the row string with 'Q' at c
                row_str = '.' * c + 'Q' + '.' * (n - c - 1)
                board.append(row_str)
                
                # Recurse to next row
                backtrack(r + 1)
                
                # Backtrack: remove queen
                board.pop()
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)
        
        backtrack(0)
        return res
        