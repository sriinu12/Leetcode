from typing import List
import math

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def min_bbox_area(r1: int, r2: int, c1: int, c2: int) -> int:
            """Area of the minimal rectangle covering all 1s in submatrix; 0 if none."""
            top = math.inf
            left = math.inf
            bottom = -1
            right = -1
            for r in range(r1, r2 + 1):
                row = grid[r]
                for c in range(c1, c2 + 1):
                    if row[c] == 1:
                        if r < top:    top = r
                        if c < left:   left = c
                        if r > bottom: bottom = r
                        if c > right:  right = c
            if top is math.inf:  # no ones
                return 0
            return (bottom - top + 1) * (right - left + 1)

        INF = 10**9
        ans = INF

        # -------- L-splits (4 orientations) --------
        # 1) cut at row i; bottom part split at col j -> top | (bottom-left + bottom-right)
        for i in range(m):
            top_area = min_bbox_area(0, i, 0, n - 1)
            for j in range(n):
                left_bottom  = min_bbox_area(i + 1, m - 1, 0, j)
                right_bottom = min_bbox_area(i + 1, m - 1, j + 1, n - 1)
                ans = min(ans, top_area + left_bottom + right_bottom)

        # 2) cut at row i; top/bottom swapped
        for i in range(m):
            bottom_area = min_bbox_area(i, m - 1, 0, n - 1)
            for j in range(n):
                left_top  = min_bbox_area(0, i - 1, 0, j)
                right_top = min_bbox_area(0, i - 1, j + 1, n - 1)
                ans = min(ans, bottom_area + left_top + right_top)

        # 3) cut at col j; right part split at row i -> left | (top-right + bottom-right)
        for j in range(n):
            left_area = min_bbox_area(0, m - 1, 0, j)
            for i in range(m):
                top_right    = min_bbox_area(0, i, j + 1, n - 1)
                bottom_right = min_bbox_area(i + 1, m - 1, j + 1, n - 1)
                ans = min(ans, left_area + top_right + bottom_right)

        # 4) cut at col j; left/right swapped
        for j in range(n):
            right_area = min_bbox_area(0, m - 1, j, n - 1)
            for i in range(m):
                top_left    = min_bbox_area(0, i, 0, j - 1)
                bottom_left = min_bbox_area(i + 1, m - 1, 0, j - 1)
                ans = min(ans, right_area + top_left + bottom_left)

        # -------- Three stripes --------
        # 5) three horizontal bands: rows [0..i1], [i1+1..i2], [i2+1..m-1]
        for i1 in range(m):
            for i2 in range(i1 + 1, m):
                a = min_bbox_area(0, i1, 0, n - 1)
                b = min_bbox_area(i1 + 1, i2, 0, n - 1)
                c = min_bbox_area(i2 + 1, m - 1, 0, n - 1)
                ans = min(ans, a + b + c)

        # 6) three vertical bands: cols [0..j1], [j1+1..j2], [j2+1..n-1]
        for j1 in range(n):
            for j2 in range(j1 + 1, n):
                a = min_bbox_area(0, m - 1, 0, j1)
                b = min_bbox_area(0, m - 1, j1 + 1, j2)
                c = min_bbox_area(0, m - 1, j2 + 1, n - 1)
                ans = min(ans, a + b + c)

        return ans
