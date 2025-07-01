class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # 1. Initialize trackers and collect empty cells
        rows = [[False]*10 for _ in range(9)]
        cols = [[False]*10 for _ in range(9)]
        boxes = [[False]*10 for _ in range(9)]
        empties = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r, c))
                else:
                    d = int(board[r][c])
                    rows[r][d] = cols[c][d] = True
                    b = (r//3)*3 + (c//3)
                    boxes[b][d] = True

        def backtrack(idx: int) -> bool:
            # If all empties are filled, we’re done
            if idx == len(empties):
                return True

            r, c = empties[idx]
            b = (r//3)*3 + (c//3)
            for d in range(1, 10):
                if not rows[r][d] and not cols[c][d] and not boxes[b][d]:
                    # Place digit d
                    board[r][c] = str(d)
                    rows[r][d] = cols[c][d] = boxes[b][d] = True

                    # Recurse
                    if backtrack(idx + 1):
                        return True

                    # Backtrack
                    board[r][c] = '.'
                    rows[r][d] = cols[c][d] = boxes[b][d] = False

            # No valid digit found here → trigger backtrack
            return False

        backtrack(0)
        """
        Do not return anything, modify board in-place instead.
        """
        