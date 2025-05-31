class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        
        def get_coordinates(s: int) -> (int, int):
            """
            Given a square number s in [1..n^2], return (row, col) in the board.
            Zigzag numbering: bottom row left-to-right, next row right-to-left, etc.
            """
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            # If quot is even: left-to-right; else: right-to-left
            if quot % 2 == 0:
                col = rem
            else:
                col = n - 1 - rem
            return row, col

        # BFS queue: (square_number, moves_so_far)
        queue = deque([(1, 0)])
        visited = {1}

        while queue:
            s, moves = queue.popleft()
            # Try all possible die rolls
            for roll in range(1, 7):
                nxt = s + roll
                if nxt > target:
                    continue

                r, c = get_coordinates(nxt)
                # If there's a snake/ladder, jump
                if board[r][c] != -1:
                    nxt = board[r][c]
                
                if nxt == target:
                    return moves + 1
                
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, moves + 1))
        
        # If we exhaust all possibilities without reaching n^2:
        return -1

        