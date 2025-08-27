class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Diagonal directions in clockwise order: NE, SE, SW, NW
        DIRS = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

        @lru_cache(None)
        def dfs(i: int, j: int, turned: int, expect: int, dir_idx: int) -> int:
            # Out of bounds or value mismatch → stop
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != expect:
                return 0

            # Next expected value alternates between 2 and 0
            next_expect = 0 if expect == 2 else 2

            # Option 1: keep going straight
            di, dj = DIRS[dir_idx]
            best = 1 + dfs(i + di, j + dj, turned, next_expect, dir_idx)

            # Option 2: take one clockwise turn (only once)
            if turned == 0:
                next_dir = (dir_idx + 1) % 4
                ndi, ndj = DIRS[next_dir]
                best = max(best, 1 + dfs(i + ndi, j + ndj, 1, next_expect, next_dir))

            return best

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # Start length includes this '1'; step to first cell expecting '2'
                    for d, (di, dj) in enumerate(DIRS):
                        ans = max(ans, 1 + dfs(r + di, c + dj, 0, 2, d))
        return ans
        