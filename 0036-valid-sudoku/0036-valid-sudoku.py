class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    continue
                mask = 1 << (ord(ch) - ord('1'))  # bit 0 for '1', bit 8 for '9'
                b = (r // 3) * 3 + (c // 3)
                if (rows[r] & mask) or (cols[c] & mask) or (boxes[b] & mask):
                    return False
                rows[r] |= mask
                cols[c] |= mask
                boxes[b] |= mask
        return True
        