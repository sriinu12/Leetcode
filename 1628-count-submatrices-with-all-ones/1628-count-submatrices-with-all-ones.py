class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0

        n, m = len(mat), len(mat[0])
        heights = [0] * m
        ans = 0

        for r in range(n):
            # Update histogram heights
            for c in range(m):
                heights[c] = heights[c] + 1 if mat[r][c] == 1 else 0

            # Monotonic stack: (height, widthCount)
            stack = []
            row_sum = 0  # submatrices ending at this row up to current col

            for h in heights:
                width = 1
                # Maintain increasing heights; merge widths and remove old contrib
                while stack and stack[-1][0] >= h:
                    ph, pw = stack.pop()
                    row_sum -= ph * pw
                    width += pw

                stack.append((h, width))
                row_sum += h * width
                ans += row_sum

        return ans
        